import collections
from typing import List
import re


# 가장 흔한 단어
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))

# 입력값에는 대소문자가 섞여 있으며 쉼표 등 구두점이 존재하낟. 따라서 데이터 클렌징이 필요하다.
# 정규식에서 \w는 단어문자를 뜻하며 ^은 not을 의미한다. 위의 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.
