n, l = map(int, input().split())
funk = list(map(int, input().split()))
funk.sort()

covered = 0
result = 0

for f in funk:
  if f > covered:
    result += 1
    covered = f + l - 1

print(result)