# 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴없이 리스트 내부를 직접 조작하라
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)


Solution().reverseString(["안", "녕", "하", "세", "요"])
# 투 포인터를 이용한 전통적인 방식으로 풀이해본다.
# 단어 그대로 2개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식을 말한다.

# 파이썬다운 방식
# 이 문제는 파이썬의 기본 기능을 이용하면 단 한줄로 쉽게 풀이할 수 있다.


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        print(s.reverse())


Solution2().reverseString(["안", "녕", "하", "세", "요"])
# reverse()는 리스트에만 제공된다. 만약 입력값이 문자열이라면 앞서 살펴본 바와 같이 문자열 슬라이싱을 사용할 수 있따.
# 슬라이싱은 리스트에도 사용할 수 있으며 성능 또한 매우 좋다.
# s = s[::-1]
# 그러나 이 풀이는 릿코드에서는 오류가 발생한다. 원래는 [::-1]도 정상적으로 처리되어야 하지만
# 이 문제는 공간 복잡도를 O(1)로 제한하다 보니 변수 할당을 처리하는 데 다소 제약이 있다.
# 이 때 다음과 같은 트릭을 사용하면 잘 동작한다.
# s[:] = s[::-1]


class Solution3:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]


Solution2().reverseString(["안", "녕", "하", "세", "요"])
