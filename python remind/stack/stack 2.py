def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:
            # Если это закрывающая скобка, проверяем соответствие со стеком
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # Если это открывающая скобка, добавляем её в стек
            stack.append(char)
    
    # Если стек пустой, значит, все скобки корректно закрыты
    return not stack

# Пример использования
s = "{[()()]}"
print(is_valid_parentheses(s))  # Вывод: True
