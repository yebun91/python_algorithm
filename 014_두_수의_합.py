# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
from typing import List

nums = [2, 7, 11, 15]
target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


print(Solution().twoSum(nums, target))
# 부르트 포스로 계산.
# 배열을 2번 반복하면서 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식인 브루트 포스로 확인 할 수 있다.
# 이 경우 풀이 시간 복잡도는 O(n2)이다. 문제가 풀리기는 하지만 지나치게 느리다.
# 좀 더 최적화 할 수 있는 방안을 고민해야 한다.


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # enumerate : 인덱스와 원소를 동시에 접근하면서 루프를 돌릴 수 있음.
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]
# 여기서 in의 시간복잡도는 O(n)이고 전체 시간복잡도는 이전과 동일한 O(n2)이다.
# 그런데 여기서는 같은 시간복잡도라도 in연산 쪽이 훨씬 더 가볍고 빠르다.


print(Solution2().twoSum(nums, target))


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i  # {2:0, 7:1, 11:2, 15:3}

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
# 이 경우 타겟에서 첫 번째 수를 빼면 두 번째 수를 바로 알아낼 수 있다.
# 그렇다면 두 번째 수를 키로 하고 기존의 인텍스는 값으로 바꿔서 딕셔너리로 저장해두면 나중에 두번 째 수를 키로 조회해서 정답을 즉시 찾아낼 수 있을것이다.


print(Solution3().twoSum(nums, target))


class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
# 하나의 for문으로 합쳐서 처리해보자. 성능적인 이점은 없다.


print(Solution4().twoSum(nums, target))
