class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lettersMap_s = {}
        lettersMap_t = {}
        for char in s:
            if char not in lettersMap_s:
                lettersMap_s[char] = 1
            else:
                lettersMap_s[char] += 1
        
        for char in t:
            if char not in lettersMap_t:
                lettersMap_t[char] = 1
            else:
                lettersMap_t[char] += 1

        if lettersMap_s == lettersMap_t:
            return True
        return False
            