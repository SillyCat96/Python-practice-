def nearest_smaller_left(arr):
    stack = []
    result = []
    
    for num in arr:
        # Удаляем из стека элементы, которые больше текущего
        while stack and stack[-1] >= num:
            stack.pop()
        
        # Если стек не пуст, ближайший меньший элемент — верхний элемент стека
        if stack:
            result.append(stack[-1])
        else:
            result.append(None)
        
        # Добавляем текущий элемент в стек
        stack.append(num)
    
    return result


# Пример использования
arr = [2, 1, 4, 3, 6]
print(nearest_smaller_left(arr))  # Вывод: [None, None, 1, 1]

