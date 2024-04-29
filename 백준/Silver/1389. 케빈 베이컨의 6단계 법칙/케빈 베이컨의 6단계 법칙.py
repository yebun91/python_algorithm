from collections import deque

n, m = map(int, input().split())
sortList = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  sortList[a].append(b)
  sortList[b].append(a)

def bfs(num):
  check = [-1] * (n + 1)
  check[num] = 0
  queue = deque([num])
  
  while queue:
    current = queue.popleft()
    current_distance = check[current]
    for friend in sortList[current]:
      if check[friend] == -1 :
        check[friend] = current_distance + 1
        queue.append(friend)

  return sum(filter(lambda x: x != -1, check)) 

kevin_bacon_numbers = []

for i in range(1, n+1):
  kevin_bacon_numbers.append(bfs(i))

min_kevin_bacon_number = min(kevin_bacon_numbers)
index = kevin_bacon_numbers.index(min_kevin_bacon_number) + 1
print(index)