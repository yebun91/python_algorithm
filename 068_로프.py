n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse = True)
result = 0

for i in range(n):
  weight = rope[i] * (i + 1)
  result = max(weight, result)

print(result)
