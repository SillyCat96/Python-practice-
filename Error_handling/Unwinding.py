"""
Происходит исключение в функции A.
Если в A нет блока try...except, который может обработать исключение, выполнение A немедленно прекращается.
Python возвращается к функции, которая вызвала A (например, B).
Если в B есть блок try...except, который может обработать исключение, выполняется код обработки исключения в B. Если такого блока нет, выполнение B прекращается, и Python возвращается к функции, вызвавшей B, и так далее.
Этот процесс продолжается, пока не будет найден блок try...except, который может обработать исключение, или пока не будет достигнут верхний уровень стека вызовов (в этом случае программа завершается с необработанным исключением).
"""



def function_a():
    print("Начало function_a")
    raise ValueError("Произошла ошибка в function_a")  # Генерируем исключение
    print("Конец function_a")  # Эта строка не будет выполнена

def function_b():
    print("Начало function_b")
    function_a()
    print("Конец function_b")  # Эта строка не будет выполнена

def function_c():
    print("Начало function_c")
    try:
        function_b()
    except ValueError as e:
        print(f"Исключение перехвачено в function_c: {e}")
    print("Конец function_c")

function_c()
# Вывод:
# Начало function_c
# Начало function_b
# Начало function_a
# Исключение перехвачено в function_c: Произошла ошибка в function_a
# Конец function_c