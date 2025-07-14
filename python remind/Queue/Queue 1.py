from collections import deque

queue = deque()
queue.append(1)    # Enqueue
queue.append(2)
print(queue.popleft())  # Dequeue: 1
print(queue)           # Оставшиеся элементы: deque([2])
