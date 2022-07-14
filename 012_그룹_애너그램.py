# 문자열 배열을 받아 애너그램 단위로 그룹핑하라.
# 애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다.

import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      # defaultdict 객체
      # 존재하지 않는 키를 조회할 경우 에러메시지를 출력하는 대신
      # 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.
        anagrams = collections.defaultdict(list)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            # 딕셔너리 객체인 anagrams에 word를 sort 시킨 값을 키로 word를 넣음
        return list(anagrams.values())
        # anagrams의 value 값들을 list로 변환하여 return 함.


input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(input_strs))
# sorted()는 문자열도 잘 정렬하며 결과를 리스트 형태로 리턴하는데 이럴 다시 키로 사용하기 위해 join으로 합쳐서 이 값을 키로 사용하는 딕셔너리로 구성한다.
# 애너그램끼리는 같은 키를 갖게 되고 따라서 여기에 append()하는 형태가 된다.
# 정렬한 값을 키로 하여 딕셔너리에 추가한다. 만약 존재하지 않는 키를 삽입하려 할 경우 keyError가 발생하므로
# 에러가 나지 않도록 다음과 같이 항상 디폴트를 생성해주는 defaultdict()로 선언하며,
# 매번 키 존재 여부를 체크하지 않고 비교구문을 생략해 간결하게 구성한다.

# 여러가지 정렬 방법
# 파이썬은 정렬 함수를 기본으로 제공한다.
a = [2, 5, 1, 9, 7]
print(sorted(a))
b = "fedcba"
print(sorted(b))

# 다시 문자열로 결합하려면 다음과 같이 join()을 이용할 수 있다.
print("".join(sorted(b)))
a.sort()  # sort()는 제자리 정렬
alist = a.sort()  # 잘못된 구문, sort()함수는 None을 리턴하므로 주의

# sorted()는 또한 key= 옵션을 지정해 정렬을 위한 키 또는 함수를 별도로 지정할 수 있다.
# 다음 코드는 정렬을 위한 함수로 길이를 구하는 len을 지정한 경우다.
c = ['ccc', 'aaa', 'd', 'bb']
print(sorted(c, key=len))
# 이경우 문자열의 알파벳 순서가 아닌 길이 순서로 정렬된다.

# 함수를 이용해 키를 정의하는 방법을 좀 더 살펴보자.
# 다음은 함수를 이용해 첫 문자열(s[0])과 마지막 문자열 (s[-1]) 순으로 정렬하도록 지정했다.
d = ['cde', 'cfc', 'abc']


def fn(s):
    return s[0], s[-1]


print(sorted(d, key=fn))

# 다음과 같이 람다를 이용하면 함수를 별도로 정의하지 않고 한 줄로 처리할 수 있다.
print(sorted(d, key=lambda s: (s[0], s[-1])))
