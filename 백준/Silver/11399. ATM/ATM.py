n = int(input())
w = list(map(int, input().split()))
sortW = sorted(w)
addNum = 0
result = 0
for m in sortW :
  addNum += m
  result += addNum

print(result)