import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# 입력 값: 4(정점의 개수) 5(간선의 개수) 1(탐색을 시작할 수)
# 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

#                  1
#               /  |  \
#              2   3   |
#              \   |   |
#               \  |  /
#                  4      

# 그래프 생성 및 초기화 함수
def create_graph(N, edges):
    # N은 정점의 개수 (1,2,3,4)총 4개가 있음 
    # edges는 [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
    graph = [[] for _ in range(N + 1)] # [[], [], [], [], []] N + 1을 하는 이유는 사용하지 않을 0번째를 만들기 위해
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)
    for connections in graph:
        connections.sort()  # 정점 번호가 작은 것부터 방문하기 위해 정렬
                    # (1, 2) 일 때 graph[1]에 2를 넣음, graph[2]에 1을 넣음.
                    # (1, 3) 일 때 graph[2]에 3을 넣음, graph[3]에 1을 넣음.
    print(graph)    # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
    return graph

# DFS 구현
def dfs(graph, V, visited):
    # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]], 탐색을 시작할 정점의 수, [False, False, False, False, False]
    visited[V] = True # [False, True, False, False, False]
    print(V, end=' ')
    for next_vertex in graph[V]:
        if not visited[next_vertex]:
            dfs(graph, next_vertex, visited)

# BFS 구현
def bfs(graph, V):
    # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]], 탐색을 시작할 정점의 수
    # [False, False, False, False, False]
    visited = [False] * (len(graph))
    queue = deque([V]) # 
    visited[V] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for next_vertex in graph[vertex]:
            if not visited[next_vertex]:
                visited[next_vertex] = True
                queue.append(next_vertex)

# 입력 받기
N, M, V = map(int, input().split())
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split()))) 

# 그래프 생성
graph = create_graph(N, edges)

# 방문 여부를 확인할 리스트
visited = [False] * (N + 1)

# DFS와 BFS 수행
print("DFS:", end=' ')
dfs(graph, V, visited)
print("\nBFS:", end=' ')
bfs(graph, V)