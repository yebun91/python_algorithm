import sys
input = lambda: sys.stdin.readline().strip()

noListen, noSee = map(int, input().split())
dix = {}

for _ in range(noListen) :
  name = input()
  if name not in dix:
    dix[name] = 1

result = []

for _ in range(noSee):
  name = input()
  if name in dix:
    result.append(name)

result = sorted(result)

print(len(result))
for x in result:
  print(x)