n = int(input())
check = {}
numbers = list(map(int, input().split()))

for num in numbers:
  if num in check:
    check[num] = check[num] + 1
  else: check[num] = 1

m = int(input())
compare = list(map(int, input().split()))

result = []

for num in compare:
  if num in check:
    result.append(check[num])
  else: result.append(0)

print(*result)
