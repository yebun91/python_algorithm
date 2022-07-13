from typing import List

# 로그를 재정렬하라. 기준은 다음과 같다.
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일한 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

# 요구조건을 얼마나 깔끔하게 처리할 수 있는지를 묻는 문제다.
# 먼저 문자로 구성된 로그가 숫자 로그보다 이전에 오며, 숫자 로그는 입력 순서대로 둔다.
# 그렇다면 문자와 숫자를 구분하고 숫자는 나중에 그대로 이어 붙인다.
# 로그 자체는 숫자 로그도 모두 문자열로 지정되어 있으므로 타입을 확인하면 모두 문자로 출력된다.
# 따라서 isdigit()을 이용해서 숫자 여부인지를 판별해 구분해본다.


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []  # 문자로 된 로그와 숫자로 된 로그를 따로 넣을 list 생성
        for log in logs:
            if log.split()[1].isdigit():  # 문자를 공백 기준으로 나누고 두 번째 문자가 숫자인지 판별
                digits.append(log)  # 숫자일 경우 숫자에 리스트에 append 함
            else:
                letters.append(log)  # 아닐경우 문자 리스트에 append 함
        # 식별자를 제외한 문자열 [1:]을 키로 하여 정렬하며, 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록 람다를 이용함.
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits  # 이제 모두 이어붙여서 다음과 같이 리턴


print(Solution().reorderLogFiles(
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))

# 람다 표현식
# 람다 표현식이란 식별자 없이 실행 가능한 함수를 말하며, 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있다.
# letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
# 만약 s가 ['2 A', '1 B', '4 C', '1 A'] 라면 sorted()로 정렬한 결과는 다음과 같다.
# ['1 A', '1 B', '2 A', '4 C']
# 그러나 우리가 원하는 결과는 각 요소의 번호 순 정렬이 아닌 그 뒤의 문자 순 정렬을 원하며, 문자가 동일한 경우에만 그 앞 번호순으로 정렬되는 형태를 희망한다.
# 이 때 리스트의 각 요소를 풀어서 별도 처리를 해줘야 하는데 이럴 때 람다 표현식을 사용할 수 있다. 쉽게 말해 람다는 간단한 함수를 쉽게 선언하는 방법이라 할 수 있다.
# 만약 람다를 사용하지 않고 직접 함수를 선언한다면 다음과 같은 형태가 된다.
s = ['2 A', '1 B', '4 C', '1 A']


def func(x):
    return x.split()[1], x.split()[0]


s.sort(key=func)
print(s)
