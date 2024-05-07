n = int(input())
tip = [int(input()) for _ in range(n)]
tip.sort(reverse=True)

result = 0
for i in range(n):
  addTip = tip[i] - i
  if addTip > 0 : result += addTip 

print(result)