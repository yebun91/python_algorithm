import sys
input = sys.stdin.readline

n = int(input())
w = [] #[[일을 하는데 걸리는 시간, 이 시간 전까지 끝내야 함]]

for _ in range(n):
  t, s = map(int, input().split())
  w.append([t, s])

w.sort(key=lambda x: x[1], reverse=True)
# [[5, 20], [1, 16], [8, 14], [3, 5]]
# 20시에 모든 일이 끝나도록 함.
result = w[0][1]

for work in w:
  result = min(result, work[1]) - work[0] # 일을 수행하고 난 후의 시작 시간 업데이트
  if result < 0 :
    result = -1
    break

print(result)