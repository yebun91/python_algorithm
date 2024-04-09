n = int(input())
result = 0
add = 0
if n == 1: print(1)
else :
  for i in range(1, n):
    result = i
    add += i
    if add == 0:
      break
    if add > n:
      result -= 1
      break

  print(result)
