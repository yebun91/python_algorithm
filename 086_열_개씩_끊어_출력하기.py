a = input()
for i in range(len(a)):
  if i != 0 and (i + 1) % 10 == 0:
    print(a[i])
  else: print(a[i], end="")
  