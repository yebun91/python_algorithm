import math

n = int(input())
print("long " * (n // 4) + "long" * (n % 4 != 0) + " int")