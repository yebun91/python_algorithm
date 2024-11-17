def find_prime(M, N):
    result = []

    for number in range(M, N+1):
        if number > 1:
            for i in range(2, number):
                if i * i <= number  and number % i == 0:
                    break

            else: result.append(number)

    if len(result) == 0: print(-1)
    else:
        print(sum(result))
        print(min(result))

M = int(input())
N = int(input())

find_prime(M, N)