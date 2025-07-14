def merge_sort(arr):
    if len(arr) > 1:
        # Разделяем массив пополам
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем каждую половину
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Слияние отсортированных половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Добавляем оставшиеся элементы
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Пример использования:
arr = [5, 2, 4]
merge_sort(arr)
print("Отсортированный массив:", arr)