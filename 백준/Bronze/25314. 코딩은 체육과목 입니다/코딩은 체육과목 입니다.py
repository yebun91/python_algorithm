import math

n = int(input())
long_count = math.ceil(n / 4)
result = "long " * long_count + "int"
print(result.strip())