class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {"".join(sorted(strs[0])): [strs[0]]}

        for i in range(1, len(strs)):
            if "".join(sorted(strs[i])) in t:
                t["".join(sorted(strs[i]))].append(strs[i])
            else:
                t["".join(sorted(strs[i]))] = [strs[i]]

        res = []
        for key in t:
            res.append(t[key])
        return res
