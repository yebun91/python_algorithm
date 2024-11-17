def find_prime(N, M):
    result = 0
    for num in M:
        if num > 1 :
            for i in range(2, num):
                if num % i == 0:
                    break
            else: result += 1

    print(result)


n = int(input())


numbers = list(map(int, input().split()))
find_prime(n, numbers)