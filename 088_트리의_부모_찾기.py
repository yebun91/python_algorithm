import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n - 1)]
lists = [[] for _ in range(n + 1)]
for i,j in graph:
  lists[i].append(j)
  lists[j].append(i)

print(lists)

def bfs(): 
  result = [0] * (n + 1)
  check = [False] * (n + 1)
  check[1] = True
  queue = deque([1])

  while queue:
    num = queue.popleft()
    for neig in lists[num]:
      if not check[neig]:
        result[neig] = num
        check[neig] = True
        queue.append(neig)

  return result

d = bfs()

for i in range(2, n+1):
  print(d[i])

