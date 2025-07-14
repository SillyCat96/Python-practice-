import os

def process_file(filename):
    """
    Обрабатывает файл, демонстрируя try...except...finally.

    Args:
        filename: Имя файла для обработки.
    """
    file = None  # Инициализируем file как None
    try:
        # Попытка открыть файл для чтения
        file = open(filename, "r")
        print(f"Файл '{filename}' успешно открыт.")

        # Попытка прочитать и обработать содержимое файла
        for line in file:
            # Преобразуем строку в целое число (может вызвать ValueError)
            try:
                number = int(line.strip())
                print(f"Обработано число: {number}")
            except ValueError as e:
                print(f"Ошибка преобразования строки '{line.strip()}' в число: {e}")

        # Попытка выполнить операцию, которая может вызвать ZeroDivisionError
        try:
            result = 10 / 1  # Замените на 10 / 0 для демонстрации ZeroDivisionError
            print(f"Результат деления: {result}")
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль!")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
    finally:
        # Гарантированно закрываем файл, если он был открыт
        if file is not None:
            file.close()
            print(f"Файл '{filename}' закрыт.")
        else:
            print("Файл не был открыт, поэтому закрытие не требуется.")


# Пример использования
process_file("my_file.txt") # Замените на существующий или несуществующий файл
# Создадим файл если его не существует
if not os.path.exists("my_file.txt"):
    with open("my_file.txt", "w") as f:
        f.write("1\n2\n3\n4\nhello\n5\n")

process_file("non_existent_file.txt")