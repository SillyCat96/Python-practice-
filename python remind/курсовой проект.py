import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sqlite3
from scipy.interpolate import splrep, splev
import numpy as np
from matplotlib.backend_bases import MouseEvent
import webbrowser


# Установление соединения с базой данных
conn = sqlite3.connect('components.db')  # Замените 'hardware.db' на путь к вашей базе данных
cursor = conn.cursor()

# Функция для получения данных о компонентах (GPU или CPU)
def fetch_components(table_name):
    cursor.execute(f"SELECT name, performance, price_history, rating, price_performance, manufacturer, link FROM {table_name}")
    components = cursor.fetchall()
    return components

# Получение данных из таблиц GPU и CPU
gpu_data = fetch_components('gpu')
cpu_data = fetch_components('cpu')


# Функция для обработки клика по ссылке
def open_link(event, link):
    webbrowser.open(link)

# Функция для вывода истории цен для конкретного компонента
def print_price_history(data, index, text_widget, price_history_canvas):
    price_history = eval(data[index][2])  # Преобразуем строку с ценовой историей обратно в список
    link = data[index][6]  # Извлекаем ссылку на товар
    initial_price = price_history[0]
    current_price = price_history[-1]

    # Очистить текстовый виджет перед выводом новой информации
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, f"Price History for {data[index][0]}:\n")
    text_widget.insert(tk.END, f"Starting Price: {initial_price}\n")

    # Добавление кликабельной ссылки
    text_widget.insert(tk.END, "Link: ", "normal")
    text_widget.insert(tk.END, f"{link}\n", "link")

    # Создание тега для ссылки
    text_widget.tag_config("link", foreground="blue", underline=True)
    text_widget.tag_bind("link", "<Button-1>", lambda e: open_link(e, link))

    # Плавная интерполяция для цены
    x = np.arange(len(price_history))
    spl = splrep(x, price_history, s=0)  # Интерполяция сплайном
    smooth_price_history = splev(x, spl)

    # Построение графика для истории цен
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(smooth_price_history, color='blue')
    ax.set_title(f"Price History for {data[index][0]}")
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    ax.grid(True)

    # Отображение графика в Tkinter
    for widget in price_history_canvas.winfo_children():
        widget.destroy()  # Удаление старых графиков

    canvas = FigureCanvasTkAgg(fig, master=price_history_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Вывод изменений цен с цветами
    for i in range(1, len(price_history)):
        price_change = price_history[i] - price_history[i-1]
        percent_change = round((price_change / price_history[i-1]) * 100, 2)
        
        # Используем зеленый цвет для уменьшения, красный для увеличения
        if price_change > 0:
            text_widget.insert(tk.END, f"{price_history[i]} (Increased by {price_change} ({percent_change}%))\n", 'red')
        else:
            text_widget.insert(tk.END, f"{price_history[i]} (Decreased by {price_change} ({percent_change}%))\n", 'green')
    
    text_widget.insert(tk.END, f"Current Price: {current_price}\n")




# Функция для подбора компонентов по цене
def find_by_price():
    selected_category = category_combobox.get()  # Получаем выбранную категорию из выпадающего списка
    
    if selected_category == "GPU":
        data = gpu_data
    elif selected_category == "CPU":
        data = cpu_data
    else:
        messagebox.showerror("Ошибка", "Неверная категория!")
        return
    
    # Сортировка компонентов по цене (по возрастанию)
    sorted_data = sorted(data, key=lambda x: eval(x[2])[-1])  # сортируем по последней цене из истории
    update_table(sorted_data)  # Обновляем таблицу с отсортированными компонентами

# Функция для подбора компонентов по производительности
def find_by_performance():
    selected_category = category_combobox.get()  # Получаем выбранную категорию из выпадающего списка
    
    if selected_category == "GPU":
        data = gpu_data
    elif selected_category == "CPU":
        data = cpu_data
    else:
        messagebox.showerror("Ошибка", "Неверная категория!")
        return
    
    # Сортировка компонентов по производительности (по убыванию)
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)  # сортируем по производительности
    update_table(sorted_data)  # Обновляем таблицу с отсортированными компонентами


# Функция для отображения графика "Цена vs Производительность" с зонами
def show_category_data(category):
    if category == "GPU":
        data = gpu_data
    elif category == "CPU":
        data = cpu_data
    else:
        return  # Если не выбран правильный category, выходим

    messagebox.showinfo(category, f"Вы выбрали категорию {category}. Здесь будут показаны компоненты {category}.")
    
    # Сортируем компоненты по цене
    prices = []
    performances = []
    price_performance_ratios = []  # Список для соотношений цена/производительность
    names = []  # Список для имен компонентов
    for component_data in data:
        name = component_data[0]  # Название компонента
        price_history = eval(component_data[2])  # Преобразуем строку с ценовой историей обратно в список
        current_price = price_history[-1]  # Текущая цена (последняя в истории)
        performance = component_data[1]  # Производительность
        price_performance_ratio = performance / current_price  # Соотношение цена/производительность

        prices.append(current_price)
        performances.append(performance)
        price_performance_ratios.append(price_performance_ratio)
        names.append(name)

    # Сортировка по цене
    sorted_data = sorted(zip(prices, performances, price_performance_ratios, names), key=lambda x: x[0])
    sorted_prices, sorted_performances, sorted_price_performance_ratios, sorted_names = zip(*sorted_data)

    # Находим лучшее соотношение цена/производительность для каждой зоны
    best_performance_price_30000 = None
    best_performance_price_65000 = None
    best_performance_price_unlimited = None

    for i, (price, performance, ratio) in enumerate(zip(sorted_prices, sorted_performances, sorted_price_performance_ratios)):
        if price <= 30000:
            if best_performance_price_30000 is None or ratio > best_performance_price_30000[2]:
                best_performance_price_30000 = (price, performance, ratio, sorted_names[i])
        elif price <= 65000:
            if best_performance_price_65000 is None or ratio > best_performance_price_65000[2]:
                best_performance_price_65000 = (price, performance, ratio, sorted_names[i])
        else:
            if best_performance_price_unlimited is None or ratio > best_performance_price_unlimited[2]:
                best_performance_price_unlimited = (price, performance, ratio, sorted_names[i])

    # Плавная интерполяция для цен и производительности
    x = np.arange(len(sorted_prices))
    spl_price = splrep(x, sorted_prices, s=0)
    spl_performance = splrep(x, sorted_performances, s=0)
    smooth_prices = splev(x, spl_price)
    smooth_performances = splev(x, spl_performance)

    fig, ax = plt.subplots(figsize=(7, 5))
    scatter = ax.scatter(sorted_prices, sorted_performances, color='green')  # Точки
    
    # Плавная линия для цены и производительности
    ax.plot(smooth_prices, smooth_performances, color='blue')

    # Разделение графика на зоны
    ax.axvline(x=30000, color='black', linestyle='--', label='Up to 30,000')
    ax.axvline(x=65000, color='black', linestyle='--', label='Up to 65,000')

    # Выделение точек с лучшим соотношением цена/производительность для каждой зоны
    if best_performance_price_30000:
        ax.scatter(best_performance_price_30000[0], best_performance_price_30000[1], color='red', s=100, label='Best Price/Performance up to 30,000')
        # Сдвигаем на 5% влево
        ax.text(best_performance_price_30000[0] - 0.40 * best_performance_price_30000[0], best_performance_price_30000[1] + 50, best_performance_price_30000[3], color='red', fontsize=12)

    if best_performance_price_65000:
        ax.scatter(best_performance_price_65000[0], best_performance_price_65000[1], color='red', s=100, label='Best Price/Performance up to 65,000')
        # Сдвигаем на 5% вправо
        ax.text(best_performance_price_65000[0] - 0.1 * best_performance_price_65000[0], best_performance_price_65000[1] + 50, best_performance_price_65000[3], color='red', fontsize=12)

    if best_performance_price_unlimited:
        ax.scatter(best_performance_price_unlimited[0], best_performance_price_unlimited[1], color='red', s=100, label='Best Price/Performance > 65,000')
        ax.text(best_performance_price_unlimited[0] + 500, best_performance_price_unlimited[1] - 20, best_performance_price_unlimited[3], color='red', fontsize=12)

    # Обработчик события для отображения названия компонента при наведении
    def on_move(event: MouseEvent):
        contains, _ = scatter.contains(event)
        if contains:
            ind = scatter.contains(event)[1]["ind"][0]  # Индекс точки, на которой наведена мышь
            ax.set_title(f"Название: {sorted_names[ind]}")  # Показываем название компонента
            fig.canvas.draw_idle()  # Перерисовываем график

    # Подключаем обработчик события для движения мыши
    fig.canvas.mpl_connect('motion_notify_event', on_move)

    # Настройка графика
    ax.set_title('Price vs Performance')
    ax.set_xlabel('Price')
    ax.set_ylabel('Performance')
    ax.grid(True)
    ax.legend()

    # Отображение графика в Tkinter
    for widget in price_history_canvas.winfo_children():
        widget.destroy()  # Удаление старых графиков

    canvas = FigureCanvasTkAgg(fig, master=price_history_canvas)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    # Обновляем таблицу с компонентами
    update_table(data)







# Функция для обновления таблицы с компонентами
def update_table(data):
    # Очистка текущих данных в таблице
    for row in table.get_children():
        table.delete(row)

    # Заполнение таблицы новыми данными
    for component_data in data:
        table.insert("", "end", values=component_data)

# Функция для отображения истории цен по номеру компонента
def show_price_history():
    selected_category = category_combobox.get()  # Получаем выбранную категорию из выпадающего списка
    component_index = int(entry.get()) - 1  # Получаем номер компонента из ввода
    
    if selected_category == "GPU":
        data = gpu_data
    elif selected_category == "CPU":
        data = cpu_data
    else:
        messagebox.showerror("Ошибка", "Неверная категория!")
        return
    
    # Проверка на валидный индекс
    if component_index >= 0 and component_index < len(data):  
        print_price_history(data, component_index, price_history_text, price_history_canvas)
    else:
        messagebox.showerror("Ошибка", "Неверный номер компонента!")


# Создание главного окна
root = tk.Tk()
root.title("Компоненты: GPU и CPU")

# Добавление кнопок для категорий
category_label = tk.Label(root, text="Выберите категорию:")
category_label.pack(pady=10)

category_combobox = ttk.Combobox(root, values=["GPU", "CPU"])
category_combobox.pack(pady=10)
category_combobox.set("GPU")  # Устанавливаем значение по умолчанию (GPU)

# Кнопки для выбора действий
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

category_button = tk.Button(button_frame, text="Показать данные", width=20, height=2, 
                            command=lambda: show_category_data(category_combobox.get()))
category_button.pack(side=tk.LEFT, padx=5)

# Фрейм для подбора по цене
price_frame = tk.Frame(root)
price_frame.pack(pady=10)

price_label_max = tk.Label(price_frame, text="Максимальная цена:")
price_label_max.pack(side=tk.LEFT, padx=5)

max_price_entry = tk.Entry(price_frame, width=10)
max_price_entry.pack(side=tk.LEFT, padx=5)

price_button = tk.Button(price_frame, text="Подобрать по цене", width=20, height=2, command=find_by_price)
price_button.pack(pady=5)

# Фрейм для подбора по производительности
performance_frame = tk.Frame(root)
performance_frame.pack(pady=10)

performance_label = tk.Label(performance_frame, text="Минимальная мощность:")
performance_label.pack(side=tk.LEFT, padx=5)

min_performance_entry = tk.Entry(performance_frame, width=10)
min_performance_entry.pack(side=tk.LEFT, padx=5)


performance_button = tk.Button(performance_frame, text="Подобрать по мощности", width=20, height=2, command=find_by_performance)
performance_button.pack(pady=5)

# Элемент для ввода номера компонента
label = tk.Label(root, text="Введите номер компонента для отображения его истории цен:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

# Кнопка для отображения истории цен
history_button = tk.Button(root, text="Показать историю цен", width=20, height=2, command=show_price_history)
history_button.pack(pady=10)

# Виджет Text для отображения истории цен с цветами
price_history_text = tk.Text(root, width=60, height=15)
price_history_text.pack(pady=10)

# Виджет для отображения графиков
price_history_canvas = tk.Frame(root)
price_history_canvas.pack(fill=tk.BOTH, expand=True, pady=10)

# Добавление тегов для цветов
price_history_text.tag_configure('red', foreground='red')
price_history_text.tag_configure('green', foreground='green')

# Виджет Treeview для отображения таблицы
table = ttk.Treeview(root, columns=("Name", "Performance", "Price History", "Rating", "Price/Performance", "Manufacturer", "Link"), show="headings")
table.pack(pady=10, fill=tk.BOTH, expand=True)

# Настройка заголовков колонок
table.heading("Name", text="Name")
table.heading("Performance", text="Performance")
table.heading("Price History", text="Price History")
table.heading("Rating", text="Rating")
table.heading("Price/Performance", text="Price/Performance")
table.heading("Manufacturer", text="Manufacturer")
table.heading("Link", text="Link")

# Запуск GUI
root.mainloop()

# Закрытие соединения с базой данных
conn.close()
