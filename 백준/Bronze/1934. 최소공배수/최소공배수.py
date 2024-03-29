n = int(input())

def gcd(l,r):
  if r == 0:
    return l
  return gcd(r, l % r)

for _ in range(n):
  a, b = map(int, input().split())
  print(a*b//gcd(a, b))

# 유클리드호제법, 재귀함수 연습중...