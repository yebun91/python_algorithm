n = int(input())
t = list(map(int, input().split()))
t.sort()

day = t[n-1]
result = 0

while day > 0 or len(t) > 0:
  if len(t) > 0 :
    tree = t.pop()
    if tree > day : day = tree 
  day -= 1 
  result += 1 

print(result + 2) # 마지막 나무가 자란 다음 날 + 심고난 다음날부터 자라는 나무