import sys

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hobbies = [] # Список - это тоже объект, хранящийся в куче

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

# --- Создание первого экземпляра ---
print("--- Создание первого экземпляра: person1 ---")
person1 = Person("Alice", 30)

print(f"ID объекта person1: {id(person1)}")
print(f"Тип объекта person1: {type(person1)}")
print(f"Размер объекта person1 (приблизительно): {sys.getsizeof(person1)} байт")
print(f"person1.__dict__: {person1.__dict__}")

print("\n--- Добавление атрибутов ---")
# Добавление нового атрибута
person1.city = "New York"
print(f"person1.__dict__ после добавления city: {person1.__dict__}")

# Изменение существующего атрибута
person1.age = 31
print(f"person1.__dict__ после изменения age: {person1.__dict__}")

print("\n--- Работа со списком внутри экземпляра ---")
person1.add_hobby("Reading")
person1.add_hobby("Hiking")
print(f"person1.hobbies: {person1.hobbies}")
print(f"ID списка person1.hobbies: {id(person1.hobbies)}")

# --- Создание второго экземпляра ---
print("\n--- Создание второго экземпляра: person2 ---")
person2 = Person("Bob", 25)

print(f"ID объекта person2: {id(person2)}")
print(f"person2.__dict__: {person2.__dict__}")
print(f"ID списка person2.hobbies: {id(person2.hobbies)}")

# --- Сравнение экземпляров ---
print("\n--- Сравнение экземпляров ---")
print(f"person1 is person2: {person1 is person2}") # Проверяет идентичность объектов
print(f"person1.name is person2.name: {person1.name is person2.name}") # Сравнение строк (может быть True/False из-за интернирования)
print(f"person1.age is person2.age: {person1.age is person2.age}") # Сравнение чисел (может быть True/False из-за интернирования)
print(f"person1.hobbies is person2.hobbies: {person1.hobbies is person2.hobbies}") # Сравнение списков