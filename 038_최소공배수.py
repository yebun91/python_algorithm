import math

n = int(input())

for _ in range(n):
  a, b = map(int, input().split())
  print(math.lcm(a, b)) # 걍 기본함수로도 구할 수 있움...



