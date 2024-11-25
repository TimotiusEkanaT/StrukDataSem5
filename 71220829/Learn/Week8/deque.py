from collections import deque

q = deque([20, 30, 30, 40])
q.appendleft(1)
q.append(67)
print(q)
q.popleft()
print(q)
q.pop()
print(q)