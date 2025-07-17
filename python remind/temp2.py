import sys
import gc
import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None # Добавим 'prev' для демонстрации обратной ссылки
        print(f"Node {self.value} создан.")

    def __del__(self):
        print(f"Node {self.value} удален.")

def create_circular_reference_with_weakref():
    print("\n--- Демонстрация решения циклической ссылки с weakref ---")
    node_a = Node("A")
    node_b = Node("B")

    node_a.next = node_b # Сильная ссылка от A к B
    
    # КЛЮЧЕВОЕ ИЗМЕНЕНИЕ: Используем weakref.ref() для обратной ссылки
    # Теперь B ссылается на A слабой ссылкой
    node_b.prev = weakref.ref(node_a) 

    # В этом сценарии нет чистой круговой ссылки, предотвращающей сбор мусора
    # node_a.next -> node_b (сильная)
    # node_b.prev -> node_a (слабая)

    print("Круговая ссылка (с одной слабой) создана (объекты Node A и B).")
    
    # Попытка получить объект через слабую ссылку
    if node_b.prev:
        # weak_ref_target = node_b.prev() # Получаем объект, если он еще жив
        # print(f"Node B ссылается на A (через слабую ссылку): {weak_ref_target.value if weak_ref_target else 'None'}")
        pass # Не будем выводить здесь, чтобы не влиять на счетчик ссылок для чистоты эксперимента

    print(f"Ref count Node A до выхода из функции: {sys.getrefcount(node_a) - 1}")
    print(f"Ref count Node B до выхода из функции: {sys.getrefcount(node_b) - 1}")

# Запускаем функцию, где создается цикл со слабой ссылкой
create_circular_reference_with_weakref()
print("Функция create_circular_reference_with_weakref завершилась.")

# Здесь объекты Node("A") и Node("B") ДОЛЖНЫ быть удалены автоматически,
# так как слабая ссылка не удерживает их.
print("Проверяем, были ли объекты удалены без gc.collect()...")
# Если деструкторы не вызвались, значит gc еще не сработал.
# Для большей уверенности можно вызвать gc.collect(), но по идее не должно быть утечки.
gc.collect() # Для демонстрации, что даже с gc.collect(), они уже были бы удалены

print("--- Конец демонстрации ---")