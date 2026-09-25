class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters_hash = set()
        max_count = 0
        l = 0

        for r in range(len(s)):
            while s[r] in letters_hash:
                letters_hash.remove(s[l])
                l += 1
            letters_hash.add(s[r])
            max_count = max(max_count, r - l + 1)
        return max_count
                









        # for char in s:
        #     if char in letter_hash: 
        #         letter_hash.clear()
        #         max_count = max(max_count, count)
        #         count = 0
        #     else:
        #         letter_hash.add(char)
        #         count += 1
                
        # return max(max_count, count)