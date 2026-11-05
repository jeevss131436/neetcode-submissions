class Solution:
    def isValid(self, s: str) -> bool:
        validity = []
        closeOpen = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closeOpen:
                if validity and validity[-1] == closeOpen[c]:
                    validity.pop()
                else:
                    return False
            else:
                validity.append(c)
        if not validity:
            return True
        return False