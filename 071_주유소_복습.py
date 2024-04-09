n = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))

result = 0
minOil = oil[0]

for i in range(n-1):
  minOil = min(minOil, oil[i])
  result = result + (length[i]*minOil)

print(result)