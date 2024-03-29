def f(num) :
  if num <= 1 :
    return 1
  return num * f(num-1)

n = int(input())
print(f(n))