n, money = map(int, (input().split()))
coins = []
for _ in range(n):
  coins.append(int(input())) 

result = 0
while money > 0:
  minus = coins.pop()
  if money // minus > 0:
    result += money // minus
    money %= minus


print(result)