from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(m)]
sortedGraph = [[] for _ in range(n+1)]
check = [False for _ in range(n+1)]

for c,d in graph:
  sortedGraph[c].append(d)
  sortedGraph[d].append(c)

def bfs():
  queue = deque([(a, 0)])
  check[a] = True
  while queue:
    men, num = queue.popleft()
    if men == b :
      return num
    for seach in sortedGraph[men]:
      if not check[seach]:
        queue.append((seach, num+1))
        check[seach] = True
  return -1

print(bfs())



