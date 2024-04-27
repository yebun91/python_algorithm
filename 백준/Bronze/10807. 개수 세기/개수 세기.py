n = int(input())
lst = list(map(int, input().split()))
countNum = int(input())
           
obj = {}
for num in lst:
    if num in obj : obj[num] += 1
    else: obj[num] = 1

print(obj.get(countNum, 0))