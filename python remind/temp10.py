def create_list():
    my_local_variable = 10 # Локальная переменная, будет на стеке
    new_list = [1, 2, 3]   # Сам список [1, 2, 3] будет на куче
    return new_list        # Возвращаем ссылку на список

# --- Главная часть программы ---
my_data = create_list()
print(my_data)
# Теперь 'my_data' содержит ссылку на список [1, 2, 3]
# Хотя функция create_list() уже завершила свою работу,
# список [1, 2, 3] все еще существует и доступен.