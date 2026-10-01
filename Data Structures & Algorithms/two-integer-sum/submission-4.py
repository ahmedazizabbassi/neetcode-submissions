class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = {}

        for i, el in enumerate(nums):
            diff = target - el
            if diff in t:
                return [t[diff], i]
            else:
                t[el] = i

        return []
