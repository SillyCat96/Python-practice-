# Использование lambda с map() для возведения каждого элемента списка в квадрат
numbers = [1, 2, 3, 4, 5]

# map(function, iterable) - применяет функцию к каждому элементу iterable (например, списка) и возвращает итератор с результатами.
# В данном случае:
# - lambda x: x**2  - анонимная функция, которая принимает число x и возвращает его квадрат.
# - numbers - список, к каждому элементу которого будет применена lambda-функция.
# list(map(...)) - преобразует итератор, возвращенный map(), в список.
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Вывод: [1, 4, 9, 16, 25]

# Использование lambda с filter() для фильтрации четных чисел из списка
numbers = [1, 2, 3, 4, 5]

# filter(function, iterable) - создает итератор, содержащий только те элементы iterable, для которых function возвращает True.
# В данном случае:
# - lambda x: x % 2 == 0 - анонимная функция, которая принимает число x и возвращает True, если x четное, и False в противном случае.
# - numbers - список, из которого будут отфильтрованы элементы.
# list(filter(...)) - преобразует итератор, возвращенный filter(), в список.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Вывод: [2, 4]

# Использование lambda с sorted() для сортировки списка кортежей по второму элементу
data = [(1, 5), (2, 3), (3, 1)]

# sorted(iterable, key=function) - возвращает новый отсортированный список из элементов iterable.
# key - необязательный аргумент, который определяет функцию, используемую для извлечения "ключа" для сравнения элементов.
# В данном случае:
# - lambda item: item[1] - анонимная функция, которая принимает кортеж item и возвращает его второй элемент (индекс 1).
#   Таким образом, сортировка будет производиться по второму элементу каждого кортежа.
sorted_data = sorted(data, key=lambda item: item[1])
print(sorted_data)  # Вывод: [(3, 1), (2, 3), (1, 5)]