import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('components.db')  # Замените на имя вашей базы данных
cursor = conn.cursor()

# Новая ценовая история для RTX 4090
new_price_history = [275000, 270000, 265000, 260000, 255000, 273000]

# Удаляем старую историю цен для RTX 4090 и вставляем новую
cursor.execute("UPDATE gpu SET price_history = ? WHERE name = '4090'", (str(new_price_history),))

# Сохраняем изменения в базе данных
conn.commit()

# Вывод сообщения о том, что все прошло успешно
print("Ценовая история для RTX 4090 успешно обновлена.")

# Закрываем соединение с базой данных
conn.close()
