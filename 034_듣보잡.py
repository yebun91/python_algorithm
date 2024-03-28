noListen, noSee = map(int, input().split())
dict = {}

for _ in range(noListen) :
  name = input()
  if name not in dict:
    dict[name] = 1

result = []

for _ in range(noSee):
  name = input()
  if name in dict:
    result.append(name)

result = sorted(result)

print(len(result))
for x in result:
  print(x)
