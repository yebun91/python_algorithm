import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

ds = [0, 0, 0, 0, -1, 1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]

queue = deque()
y, x, s = map(int, input().split())
graph = []
for i in range(s):
    box = []
    for j in range(x):
        tomatos = list(map(int, input().split()))
        isTomato = [index for index, value in enumerate(tomatos) if value == 1]
        box.append(tomatos)
        if isTomato :
            for k in isTomato :
                queue.append((i, j, k)) 
    graph.append(box)

def bfs():
    days = -1
    while queue:
        days += 1
        for _ in range(len(queue)):
            popS, popX, popY = queue.popleft()
            for i in range(6):
                ns = popS + ds[i]
                nx = popX + dx[i]
                ny = popY + dy[i]
                if 0 <= nx < x and 0 <= ny < y and 0 <= ns < s and graph[ns][nx][ny] == 0:
                    graph[ns][nx][ny] = 1
                    queue.append((ns, nx, ny))

    for row in graph:
        for colum in row:
            if 0 in colum:
                return -1 
                    
    return days

print(bfs())