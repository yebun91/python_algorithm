import sys
input = lambda: sys.stdin.readline().strip()

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n, m = map(int, input().split())  # 입력 받기
gcd_value = gcd(n, m)  # 최대공약수 구하기

result = '1' * gcd_value  # 최대공약수만큼의 1로 이루어진 문자열 생성
print(result)  # 결과 출력