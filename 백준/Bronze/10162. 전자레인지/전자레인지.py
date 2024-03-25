time = int(input())
buttons = [300, 60, 10]
result = [0, 0, 0]

for i in range(len(buttons)):
  result[i] = time // buttons[i]
  time = time % buttons[i]
  
if time == 0 : print(*result)
else: print(-1)