def partition_subsets(nums):
    total_sum = sum(nums)

    # Если сумма нечетная, нельзя разделить на два равных подмножества
    if total_sum % 2 != 0:
        return None

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Нулевая сумма всегда возможна

    # Массив для отслеживания элементов, которые составляют целевую сумму
    prev = [-1] * (target + 1)

    # Итерация по элементам массива
    for i, num in enumerate(nums):
        # Обновляем массив dp с конца
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
                prev[j] = i  # Сохраняем индекс элемента, который приводит к сумме j

    if not dp[target]:
        return None  # Если нет способа получить целевую сумму, возвращаем None

    # Восстанавливаем подмножества
    subset1 = []
    subset2 = []
    j = target

    while j > 0:
        index = prev[j]
        subset1.append(nums[index])
        j -= nums[index]

    # Элементы, которые не вошли в subset1, идут в subset2
    for k in range(len(nums)):
        if k not in subset1:
            subset2.append(nums[k])

    return subset1, subset2

# Примеры
result1 = partition_subsets([1, 5, 11, 5])
result2 = partition_subsets([1, 2, 3, 5])

print("Подмножества для [1, 5, 11, 5]:", result1)  # Ожидается вывод двух подмножеств
print("Подмножества для [1, 2, 3, 5]:", result2)   # Ожидается None
