from collections import deque 
import sys
input = lambda: sys.stdin.readline().strip()

# 1~n까지의 수가 있고 m줄의 input을 더 받는다, 시작은 v부터
n, m, v = map(int, input().split())
inputs = []
for _ in range(m):
  inputs.append(list(map(int, input().split())))

sorted_inputs = [[] for _ in range(n+1)]
for i in inputs:
  a, b = i
  sorted_inputs[a].append(b)
  sorted_inputs[b].append(a)

sorted_inputs = [sorted(innerList) for innerList in sorted_inputs]

dfsResult = []
bfsResult = []

checkList = [False for _ in range(n+1)]

def dfs(startNum):
  checkList[startNum] = True
  dfsResult.append(startNum)
  
  for nextNumber in sorted_inputs[startNum]:
    if not checkList[nextNumber]:
      checkList[nextNumber] = True
      dfs(nextNumber)

def bfs(startNum):
  checkList = [False for _ in range(n+1)]
  checkList[startNum] = True
  bfsResult.append(startNum)
  queue = deque([startNum])

  while queue:
    x = queue.popleft()
    for nextNumber in sorted_inputs[x]:
      if not checkList[nextNumber]:
        checkList[nextNumber] = True
        queue.append(nextNumber)
        bfsResult.append(nextNumber)

dfs(v)
bfs(v)
print(*dfsResult)
print(*bfsResult)

