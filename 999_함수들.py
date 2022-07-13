# 문자열 함수
# isalnum : 영문자, 숫자 여부를 판별하는 함수
import collections
import re
'a'.isalnum()  # True
'.'.isalnum()  # False

# split : 문자를 특정 문자나 공백으로 나눔.
"hi im yujin".split()  # ["hi", "im", "yujin"]
"hello.im.yuju".split(".")  # ['hello', 'im', 'yuju']

# isdigit : 문자가 숫자인지 판별함.
"19".isdigit()  # True
"zz".isdigit()  # False

# sort : 정렬, 기본값은 오름차순 정렬. reverse=True는 내림차순 정렬
[1, 10, 5, 7, 6].sort()  # [1, 5, 6, 7, 10]
[1, 10, 5, 7, 6].sort(reverse=True)  # [10, 7, 6, 5, 1]
# sort의 key 옵션, key 옵션에 지정된 함수의 결과에따라 정렬, 아래는 원소의 길이
['나는', '파이썬을', '잘하고', '싶다'].sort(key=len)

# re.sub : 정규표현식을 이용한 문자열 치환 re.sub(정규표현식, 대상문자열, 치환문자)
text = """\
010-1234-5678 Kim
011-1234-5678 Lee
016-1234-5678 Han
"""
print(re.sub('^[0-9]{3}-[0-9]{4}-[0-9]{4}', "***-****-****", text))

# 데크 선언
strs = collections.deque()
