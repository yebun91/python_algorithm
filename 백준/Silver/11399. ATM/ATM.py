n = int(input())
w = list(map(int, input().split()))
w.sort()

addNum = 0
result = 0

for num in w:
  addNum += num
  result += addNum

print(result)
