cat = int(input())
count = 0
makeCat = 0

while cat > makeCat :
  if cat == 1 :
    count += 1
    break
  else:
    if makeCat == 0: makeCat = 1
    else: makeCat *= 2
  count += 1

print(count)