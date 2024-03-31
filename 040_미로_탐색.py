from collections import deque
    # 상  하  좌  우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1 ]
queue = deque([(0, 0)]) # 큐 생성 후 초기 위치
n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
print(maze)
while queue:
    print(queue)
    x, y = queue.popleft() # 맨 처음엔 0, 0
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4): 
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나면 무시
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        # 벽인 경우 무시
        if maze[nx][ny] == 0:
            continue
        # 해당 노드를 처음 방문하는 경우에만 기록
        if maze[nx][ny] == 1:
            maze[nx][ny] = maze[x][y] + 1
            print(maze)
            queue.append((nx, ny))
            

print(maze[n-1][m-1])

# 어려워서,. 뭔 말인지 모르겠음 다시 이해해아 할듯