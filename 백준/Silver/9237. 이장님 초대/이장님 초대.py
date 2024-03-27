n = int(input())
t = list(map(int, input().split()))
t.sort()

day = t[n-1] + 1
result = 0

while day > 0 or len(t) > 0:
  if len(t) > 0 :
    tree = t.pop() + 1 
    if tree > day : day = tree 
  day -= 1 
  result += 1 

print(result + 1) # 마지막 나무가 자란 다음 날