class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sMap = {}
        tMap = {}

        for char in s:
            if char not in sMap:
                sMap[char] = 1
            else:
                sMap[char] += 1
        
        for char in t:
            if char not in tMap:
                tMap[char] = 1
            else:
                tMap[char] += 1
        
        if sMap == tMap:
            return True
        return False