def find_prime(M, N):
    sieve = [True] * (N + 1)
    sieve[0] = sieve[1] = False  

    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, N + 1, i):
                sieve[j] = False

    for i in range(M, N + 1):
        if sieve[i]:
            print(i)


M, N = map(int, input().split())
find_prime(M, N)