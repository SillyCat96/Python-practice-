def make_multiplier(factor):
    """
    Внешняя функция, которая возвращает вложенную функцию (замыкание).
    'factor' является переменной из внешней области видимости,
    которую запоминает inner_multiplier.
    """
    def inner_multiplier(number):
        return number * factor
    return inner_multiplier

# Создаем замыкания
times_five = make_multiplier(5)  # 'times_five' - это замыкание, запомнившее factor=5
times_ten = make_multiplier(10)  # 'times_ten' - это замыкание, запомнившее factor=10

print(times_five(3))  # Выведет 15 (3 * 5)
print(times_ten(3))   # Выведет 30 (3 * 10)