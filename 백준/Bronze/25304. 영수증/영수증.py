total = int(input())
n = int(input())

for _ in range(n):
    price, cnt = map(int, input().split())
    total -= price * cnt
    
if total == 0: print("Yes")
else: print("No")