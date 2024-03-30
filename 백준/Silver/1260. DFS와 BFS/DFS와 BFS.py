import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
numbers, inputCount, start = map(int, input().split())
inputNods = []
for _ in range(inputCount):
    inputNods.append(list(map(int, input().split())))

def nodeSort(n, nodes):
    graph = [[] for _ in range(n + 1)]
    for node in nodes :
        a, b = node
        graph[a].append(b)
        graph[b].append(a)
    for connections in graph:
        connections.sort()
    return graph

sortNodes = nodeSort(numbers, inputNods) 

visited = [False] * (numbers + 1)

dfsResult = []
bfsResult = []

def dfs(startNum, nodes, visited):
    visited[startNum] = True
    dfsResult.append(startNum)
    for nextVertex in nodes[startNum] :
        if not visited[nextVertex]:
            dfs(nextVertex, nodes, visited)

def bfs(startNum, nodes):
        visited = [False] * (len(nodes))
        visited[startNum] = True
        queue = deque([startNum])
        while queue:
            vertex = queue.popleft()
            bfsResult.append(vertex)

            for nextVertex in nodes[vertex] :
                if not visited[nextVertex] :
                    visited[nextVertex] = True
                    queue.append(nextVertex)

dfs(start, sortNodes, visited)
bfs(start, sortNodes)

print(*dfsResult)   
print(*bfsResult)