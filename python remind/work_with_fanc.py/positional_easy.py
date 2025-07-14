def describe_person(name, age, city="Unknown"):
    """Описывает человека."""
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

# Позиционные аргументы
describe_person("Bob", 30)  # Вывод: Имя: Bob, Возраст: 30, Город: Unknown

# Сочетание позиционных и именованных аргументов
describe_person("Charlie", 25, city="New York")  # Вывод: Имя: Charlie, Возраст: 25, Город: New York

# Неправильный порядок: именованные аргументы перед позиционными (вызовет SyntaxError)
# describe_person(name="David", 40)  # SyntaxError: positional argument follows keyword argument