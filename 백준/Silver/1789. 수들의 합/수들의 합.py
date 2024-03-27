num = int(input())
n = 0
sum = 0

result = 0

while sum <= num:
  n += 1
  sum += n
  if sum > num:
    result = n - 1 
    break
  result = n

print(result)