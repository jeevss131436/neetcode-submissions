class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_hash = set()
        l = 0
        max_count = 0

        for r in range(len(s)):
            while s[r] in letter_hash:
                letter_hash.remove(s[l])
                l += 1
            letter_hash.add(s[r])
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