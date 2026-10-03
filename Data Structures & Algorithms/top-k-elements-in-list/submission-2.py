class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        t = {}

        for num in nums:
            if num in t:
                t[num] += 1
            else:
                t[num] = 1

        arr = []
        for el, i in t.items():
            arr.append([i, el])
        arr.sort()

        res = [arr[i][1] for i in range(len(arr) - k, len(arr))]

        return res
