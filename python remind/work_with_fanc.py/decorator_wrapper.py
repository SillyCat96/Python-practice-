import time

def timer_decorator(func):
    """Декоратор для измерения времени выполнения функции."""
    def wrapper(*args,**kwargs):  # Убрали *args
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнялась {execution_time:.4f} секунд")
        return result
    return wrapper

@timer_decorator
def my_function(n, message):  # Добавили позиционный аргумент
    """Пример функции, которую нужно замерить."""
    time.sleep(n)
    return f"{message}: {n * 2}"

result = my_function(2, "Result") # Вызов с позиционным аргументом
print(f"Результат: {result}") # TypeError: my_function() got an unexpected keyword argument 'n'