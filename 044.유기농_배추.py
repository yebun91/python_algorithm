import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

repeat = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(repeat):
    m, n, k = map(int, input().split()) 
    visited = [[False] * m for _ in range(n)] 
    edges = [[0] * m for _ in range(n)] 

    for _ in range(k):
        col, row = map(int, input().split())
        edges[row][col] = 1 

    def bfs(col, row):
        visited[row][col] = True
        queue = deque([(col, row)])

        while queue:
            currentCol, currentRow = queue.popleft()
            for i in range(4):
                nx = currentCol + dx[i]
                ny = currentRow + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if edges[ny][nx] == 1 and not visited[ny][nx]:
                    queue.append((nx, ny))
                    visited[ny][nx] = True 
        return 1

    result = 0
  
    for row in range(n):
        for col in range(m):
            if edges[row][col] == 1 and not visited[row][col]:
                result += bfs(col, row)

    print(result)

