coins = [500,100,50,10,5,1]
result = 0
charge = 1000 - int(input())

for coin in coins:
  if charge == 0: break
  result += charge // coin
  charge = charge % coin
  
print(result)


