n = int(input())
l = []
for _ in range(n):
  l.append(int(input()))
result = 0
while len(l) > 0:  # 리스트 안에 데이터가 있다면 계속 반복
  num = l.pop() # 마지막 숫자를 제거함
  if len(l) > 0 and l[-1] >= num : 
    result += l[-1] - (num -1)
    l[-1] = num -1

print(result)

