n = int(input())
m = []

for _ in range(n):
  m.append(list(map(int, input().split())))

sorted_data = sorted(m, key = lambda x: sum(x[1:]))

result = 0
max_time = 0
for data in sorted_data:
  sumData = sum(data[1:])
  result += sumData + max_time
  max_time += sumData

print(result)