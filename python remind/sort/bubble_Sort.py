def bubble_sort(arr):
    n = len(arr)
    # Проходим по каждому элементу массива
    for i in range(n):
        # Внутренний цикл для сравнения соседних элементов
        for j in range(0, n - i - 1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Пример использования:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Отсортированный массив:", arr)
