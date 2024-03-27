n = int(input())
r = list(map(int, input().split()))
p = list(map(int, input().split()))

# 걍 계속 내고 가다가 제일 싼 곳이 나오면 가득 채워서 쭉 가면 됨

all = [[a, b] for a, b in zip(r, p[:-1])]
minIndex = min(range(len(all)), key=lambda i: all[i][1])
result = 0
for i in range(n-1):
  if i >= minIndex :
    result += all[i][0] * all[minIndex][1]
  else:
    result += all[i][0] * all[i][1]

print(result)