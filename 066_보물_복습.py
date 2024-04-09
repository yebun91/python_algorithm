n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sortA = sorted(a)
sortB = sorted(b, reverse=True)
result = 0

for i in range(n):
  result += (sortA[i] * sortB[i])
  
print(result)