a = input()
l = len(a)
result = 1

for i in range(l // 2):
    if a[i] != a[l - 1 - i] :
        result = 0

print(result)
        
    
    