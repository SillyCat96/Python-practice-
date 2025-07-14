def find_min(arr):
    min_val = arr[0]
    for num in arr:
        if num < min_val:
            min_val = num
    return min_val

# Ввод массива с клавиатуры
arr = list(map(int, input("Введите числа через пробел: ").split()))

# Вызываем функцию и выводим минимальное значение
print("Минимальное значение в массиве:", find_min(arr))
