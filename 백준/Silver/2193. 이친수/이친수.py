n = int(input())
count = [0] * (n+1)

for i in range(1, n+1):
  if i <= 2 : count[i] = 1
  else:
    count[i] = count[i-1] + count[i-2]

print(count[-1])