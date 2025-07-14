arr = [10, 9, 2, 5, 3, 7, 101, 18]

def longest_increasing_subarray(arr):
    max_counter = 0
    longest_subarray = []
    
    for i in range(len(arr)):
        current_subarray = [arr[i]]  # Начинаем новый подмассив с текущего элемента
        counter = 1  # Счетчик для текущего подмассива

        for j in range(i + 1, len(arr)):
            if arr[j] > current_subarray[-1]:  # Проверяем, больше ли текущий элемент последнего в подмассиве
                current_subarray.append(arr[j])  # Добавляем элемент в подмассив
                counter += 1

        # Проверяем, нужно ли обновить самый длинный подмассив
        if counter > max_counter:
            max_counter = counter
            longest_subarray = current_subarray[:]  # Сохраняем копию текущего подмассива

    return max_counter, longest_subarray

result = longest_increasing_subarray(arr)
print(result)  # Ожидаемый вывод: (4, [2, 3, 7, 101])
