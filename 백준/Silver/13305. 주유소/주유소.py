n = int(input())
r = list(map(int, input().split()))
p = list(map(int, input().split()))

result = 0
min_p = p[0]

for i in range(n-1) : 
  # 현재 가격이 min_p보다 쌀 경우 min_p 갱신
  if p[i] < min_p:
    min_p = p[i]
  result += min_p * r[i] 
  # 만나는 p[i] 값마다 min_p와 비교하면서 적으면 갱신하는 방법으로 계속 더해나감
print(result)