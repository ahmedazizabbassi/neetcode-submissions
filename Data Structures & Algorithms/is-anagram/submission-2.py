class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        ht1 = {}
        ht2 = {}

        for i in s:
            if i not in ht1:
                ht1[i] = 1
            else:
                ht1[i] += 1

        for i in t:
            if i not in ht2:
                ht2[i] = 1
            else:
                ht2[i] += 1

        for i in ht1:
            if i not in ht2 or ht2[i] != ht1[i]:
                return False
        return True
