def kadane(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)  
    return max_sum

# Пример использования: 
arr = [10, 20, 30, -40, 50]
result = kadane(arr)
print("Максимальная сумма подмассива:", result)
