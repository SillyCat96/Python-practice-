def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Выбираем опорный элемент
        pivot = arr[len(arr) // 2]
        # Все элементы меньше опорного
        left = [x for x in arr if x < pivot]
        # Все элементы равные опорному
        middle = [x for x in arr if x == pivot]
        # Все элементы больше опорного
        right = [x for x in arr if x > pivot]
        # Рекурсивно сортируем левую и правую части
        return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Отсортированный массив:", sorted_arr)
