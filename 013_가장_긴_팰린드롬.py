# 가장 긴 팰린드롬 부분 문자열을 출력하라.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            # 팰린드롬 문자를 찾았을 경우 확장해 나감
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        # 문자열 s의 길이가 1보다 작거나, s를 뒤집은 결과가 s와 같을 때 바로 s를 return
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result,      # max(str, str, key=len) : 길이가 더 긴 문자열 반환
                         expand(i, i + 1),  # 2개
                         expand(i, i + 2),  # 3개
                         key=len
                         )

        return result


print(Solution().longestPalindrome("aabreeaabreeaaee"))  # eeaaee
