def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

arr = [1, 1, 2, 4, 6,2,18,2]
target = 20

result = two_sum(arr, target)
print(result)  # Вывод: None