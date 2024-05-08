ss = []

for _ in range(5):
  ss.append(input())

result = ""

for i in range(15):
  for j in range(5):
    if i < len(ss[j]) :
      result += ss[j][i]

print(result)