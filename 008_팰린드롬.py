# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구별하지 않으며, 영문자와 숫자만을 대상으로 한다.
import collections
import re
from typing import Deque


class Solution(object):
    def isPalindrome(self, s):
      strings = []
      for char in s :
        if char.isalnum():
          strings.append(char.lower())
      while len(strings) > 1:
        if strings.pop(0) != strings.pop():
          return False
      return True

      
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))

# isalnum()는 영문자, 숫자 여부를 판별하는 함수로 이를 이용해 해당하는 문자만 추가한다.
# 대소문자를 구분하지 않으므로 lower()로 모두 소문자로 변환한다.
# 이렇게 하면 입력값이 [a, m, a, n, a, p, l, a, n, a, c, a, n, a, l, p, a, n, a, m, a]로 담기게 된다.
# 파이썬의 리스트는 pop() 함수에서 인덱스를 지정할 수 있기 때문에 이처럼 0을 지정하면 맨 앞의 값을 가져올 수 있다.
# 이렇게 맨 뒷부분의 pop() 결과와 매칭해 나가면서 일치하지 않는 경우 False를 리턴한다. 모두 통과했다면 True를 리턴한다.

# 이처럼 리스트만으로도 충분히 문제를 해결할 수 있지만, 데크를 명시적으로 선언하면 좀 더 속도를 높일 수 있다.
# 첫번째 풀이의 경우 좋은 성능이라고 보기는 어려운데, 다음과 같이 간단히 데크로 변경하는 것만으로 얼마나 개선됐는지 살펴보자.
class Solution2(object):
  def isPalindrome(self, s: str) -> bool:
    strs: Deque = collections.deque()

    for char in s : 
      if char.isalnum():
        strs.append(char.lower())

    while len(strs) > 1:
      if strs.popleft() != strs.pop():
        return False

    return True

print(Solution2().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution2().isPalindrome("race a car"))

# 여기서 strs: Dque = collectrion.deque() 와 같이 자료형을 데크로 선언하는 것만으로 64밀리초에 실행됐다.
# 이는 리스트의 pop(0)이 O(n)인 데 반해, 데크의 popleft()는 O(1)이기 때문이며, 각각 n번씩 반복하면, 리스트 구현은 O(n2), 데크 구현은 O(n)으로 성능 차이가 크다.

# 이제 파이썬의 최적화된 내부 기능을 잘 활용해 성능을 좀 더 높여보자.
class Solution3(object):
  def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]

# 여기서는 별달리 알고리즘이라 부를 만한게 없다. 정규식으로 불필요한 문자를 필터링 하고 문자열을 조작할 수 있는 파이썬의 슬라이싱을 사용했다.
# [::-1]을 이용하면 문자열을 뒤집을 수 있다. 코드가 훨씬 줄어듦은 물론 내부적으로 C로 빠르게 구현되어 있어 훨씬 더 좋은 속도를 기대할 수 있다.

# 파이썬에서는 문자열 슬라이싱이라는 매우 편리한 기능을 제공한다. 무엇보다 내부적으로 매우 빠르게 동작한다. 
# 위치를 지정하면 해당 위치의 배열 포인터를 얻게 되며 이를 통해 연결된 객체를 자아 실제 값을 찾아내는데,
# 이 과정은 매우 빠르게 진행되므로 문자열을 조작할 때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다.
# 슬라이싱 : 0.499마이크로초 
# 리스트 revers() : 2.46마이크로초
# reversed() + join() : 2.49마이크로초
# for 반복 : 5.5마이크로초
# while 반복 : 9.4마이크로초
# 재귀 : 24.3마이크로초

hi = "안녕하세요"
print(hi[1:4]) # 녕하세
print(hi[1:-2]) # 녕하
print(hi[1:]) # 녕하세요
print(hi[:]) # 안녕하세요(둘다 생략하면 사본을 리턴한다. 참조가 아닌 복사를 위해 [:]를 사용할 수 있으며 이 방식은 문자열이나 리스트를 복사하는 파이썬 다운 방식이기도 하다.)
print(hi[1:100]) # 녕하세요
print(hi[-1]) # 요
print(hi[-4]) # 녕
print(hi[:-3]) # 안녕
print(hi[-3:]) # 하세요
print(hi[::1]) # 안녕하세요
print(hi[::-1]) # 요세하녕안
print(hi[::2]) # 안하요