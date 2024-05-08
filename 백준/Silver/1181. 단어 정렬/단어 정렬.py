n = int(input())
s = [input() for _ in range(n)]

s = list(set(s))
s.sort()
s.sort(key=len)

for p in s:
  print(p)