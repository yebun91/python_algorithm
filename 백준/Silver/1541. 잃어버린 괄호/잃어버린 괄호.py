s = input().split('-')
result = sum(map(int, s[0].split('+')))

for num in s[1:]:
  result -= sum(map(int, num.split('+')))

print(result)

# 가장 작은 값을 만들기 위해서는 - 연산자 이후에 나오는 모든 숫자를 괄호로 묶어서 빼주는것이 최선의 방법
# - 연산자가 나오기 전까지의 모든 + 연산은 그대로 더해주고 - 연산자가 한번이라도 나온 이후의 모든 숫자는 괄호로 묶어서 전부 빼주면 됨.
