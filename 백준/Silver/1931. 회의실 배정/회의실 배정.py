import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]

sortM = sorted(m, key=lambda x: (x[1], x[0]))
result = 0
t = 0

for i in range(n):
  if t <= sortM[i][0]:
    result += 1
    t = sortM[i][1]
  
print(result)