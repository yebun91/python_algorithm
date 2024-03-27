num = int(input())
n = 0
sum = 0

result = 0

while sum <= num: # 모두 더한 값이 num보다 작거나 같을 때
  n += 1 # 더해갈 수를 1 플러스 함
  sum += n 
  if sum > num: # 모두 더한 수가 num보다 크다면
    result = n - 1 # 정답은 현재 더할 수 - 1
    break
  result = n

print(result)

# 예를 들어 11을 입력한다면 만들 수 있는 서로다른 자연수의 최대 개수는 총 4개임
# 1 + 2 + 3 + 5 이기 때문에 4개임!

