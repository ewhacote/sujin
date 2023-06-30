from collections import deque
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

queue.popleft()

queue.append(5)
queue.append(6)

queue.popleft()

print(queue) #최하단 원소부터 출력