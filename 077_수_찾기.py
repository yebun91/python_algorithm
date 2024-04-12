n = int(input())
check = {}
numbers = list(map(int, input().split()))

for num in numbers:
  check[num] = True

m = int(input())
compare = list(map(int, input().split()))

for num in compare:
  if num in check:
    print(1)
  else: print(0)
