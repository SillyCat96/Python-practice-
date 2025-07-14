def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum

# Пример использования функции
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(arr)
print("Максимальная сумма подмассива:", result)