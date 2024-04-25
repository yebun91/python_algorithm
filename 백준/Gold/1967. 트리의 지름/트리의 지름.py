import sys
sys.setrecursionlimit(100000)

n = int(input())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
  a, b, c = map(int, input().split())
  tree[a].append((b, c))
  tree[b].append((a, c))


def dfs(node, weight):
  global max_distance, farthest_node
  if check[node]:
    return
  check[node] = True
  if weight > max_distance:
    max_distance = weight
    farthest_node = node
  for next_node, next_weight in tree[node]:
    if not check[next_node]:
      dfs(next_node, weight + next_weight)

max_distance = 0
farthest_node = 1  
check = [False] * (n + 1)
dfs(1, 0)

max_distance = 0
check = [False] * (n + 1)
dfs(farthest_node, 0)

print(max_distance)