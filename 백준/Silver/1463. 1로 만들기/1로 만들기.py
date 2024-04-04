n = int(input())

def dpFun():
  result = 0
  dp = [n]
  while dp:
    newDp = []
    for number in dp:
      if number == 1:
        return result
      if number % 3 == 0:
        newDp.append(number // 3)
      if number % 2 == 0:
        newDp.append(number // 2)
      newDp.append(number - 1)
      dp = newDp
    result += 1

print(dpFun())