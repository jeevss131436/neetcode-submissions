class Solution:
    def isValid(self, s: str) -> bool:
        validity = []
        closeOpen = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in closeOpen:
                if validity and (validity[-1] == closeOpen[char]):
                    validity.pop()
                else:
                    return False
            else:
                validity.append(char)
        return True if not validity else False
