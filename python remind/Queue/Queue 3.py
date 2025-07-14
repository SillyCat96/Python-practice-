import heapq

priority_queue = []
heapq.heappush(priority_queue, (1, 'task1'))   # (приоритет, элемент)
heapq.heappush(priority_queue, (3, 'task3'))
heapq.heappush(priority_queue, (2, 'task2'))

print(heapq.heappop(priority_queue))  # Удаление элемента с наивысшим приоритетом: (1, 'task1')
print(priority_queue)  # Оставшиеся элементы: [(2, 'task2'), (3, 'task3')]
