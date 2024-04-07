n = int(input())
dy = [0] * (n+1)

dy[0] = 1
dy[1] = 1
for i in range(2, n+1):
    dy[i] = (dy[i-1] + 2 * dy[i-2]) % 10007

print(dy[n])

