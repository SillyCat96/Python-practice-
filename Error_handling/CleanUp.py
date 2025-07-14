def read_file_safely(filename):
    """
    Безопасно читает файл, используя with и try...except...finally.

    Args:
        filename: Имя файла для чтения.
    """
    try:
        with open(filename, "r") as f:
            print(f"Файл '{filename}' успешно открыт.")
            data = f.read()
            print(f"Содержимое файла:\n{data}")
            # Здесь может быть другая обработка данных...
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except IOError as e:
        print(f"Ошибка ввода/вывода при работе с файлом '{filename}': {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        # В данном случае finally блок не нужен для закрытия файла,
        # потому что with statement гарантирует автоматическое закрытие файла.
        # Но он может быть полезен для других действий очистки.
        print("Завершение операции чтения файла.")

# Пример использования
read_file_safely("my_file.txt")

import os
if not os.path.exists("test_file.txt"):
    with open("test_file.txt", "w") as f:
        f.write("This is a test file.\n")
        f.write("It contains some sample text.\n")

read_file_safely("non_existent_file.txt")