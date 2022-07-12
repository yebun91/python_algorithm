# 숫자 object > int > bool

# Mapping 키와 자료형으로 구성된 복합 자료형.

# 집합 set
a = set()
print(type(a))

# 빈 집합이 아닌 값이 포함된 집합을 선언할 때는
b = {1, 2, 3}  # 형태로 하는데 집합은 딕셔너리와 동일하게 중괄호를 사용하므로 이점에 유의해야 한다.
print(b)

c = {'3', '2', '1'}
print(c)

# 시퀀스
# 파이썬에서는 list라는 시퀀스 타입이 배열의 역할을 수행한다.
# 시퀀스는 불변과 가변으로 구분하는데 말 그대로 불변은 값을 변경할 수 없다.
# str, tuple, bytes가 해당됨.
d = 'abc'
print(id('abc'))
print(id(d))
d = 'def'
print(id('def'))
print(id(d))
# d[1] = 'd' 문자열을 변경 할 수 없음. error
