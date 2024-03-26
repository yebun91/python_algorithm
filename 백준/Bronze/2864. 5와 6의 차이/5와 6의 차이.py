a, b = input().split()

maxA = ""
maxB = ""
minA = ""
minB = ""

for n in a:
  if int(n) == 5:
    maxA = maxA + '6'
    minA = minA + '5'
  elif int(n) == 6:
    maxA = maxA + '6'
    minA = minA + '5'
  else: 
    maxA = maxA + str(n)
    minA = minA + str(n)

for n in b:
  if int(n) == 5:
    maxB = maxB + '6'
    minB = minB + '5'
  elif int(n) == 6:
    maxB = maxB + '6'
    minB = minB + '5'
  else: 
    maxB = maxB + str(n)
    minB = minB + str(n)

print(int(minA)+int(minB), int(maxA)+int(maxB))