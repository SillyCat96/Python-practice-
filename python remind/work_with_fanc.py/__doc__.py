# Docstring для функции
def my_function(x, y):
    """
    Эта функция складывает два числа.

    Args:
        x: Первое число.
        y: Второе число.

    Returns:
        Сумма x и y.
    """
    return x + y

print(my_function.__doc__)
# Вывод:
#
#     Эта функция складывает два числа.
#
#     Args:
#         x: Первое число.
#         y: Второе число.
#
#     Returns:
#         Сумма x и y.
#

# Docstring для класса
class MyClass:
    """
    Этот класс представляет собой пример класса.
    """
    def __init__(self, name):
        """
        Инициализирует объект класса MyClass.

        Args:
            name: Имя объекта.
        """
        self.name = name

print(MyClass.__doc__)
# Вывод:
#
#     Этот класс представляет собой пример класса.
#