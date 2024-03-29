a, b = map(int, input().split())

def xf(l, r):
  if r == 0:
    return l
  return xf(r, l % r)

x = xf(a,b) 
y = a * b // x

print(x)
print(y)