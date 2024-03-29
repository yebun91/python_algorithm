import sys
input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

def gcd(a, b):
  while b != 0:
    a, b = b, a % b
  return a

print('1' * gcd(n,m))

# 유클리드 호제법 써야한다고하네...