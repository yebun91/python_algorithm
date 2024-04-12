import heapq
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
data = [ int(input()) for _ in range(n)]

min_heap = []
result = []

for x in data:
  if x == 0:
    if min_heap:
      result.append(heapq.heappop(min_heap))
    else:
      result.append(0)
  else:
    heapq.heappush(min_heap, x)

print(*result)