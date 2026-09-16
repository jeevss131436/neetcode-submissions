class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        tempStack = []
        for i, t in enumerate(temperatures):
            while tempStack and t > tempStack[-1][0]:
                stackTemp, stackIndex = tempStack.pop()
                result[stackIndex] = (i - stackIndex)
            tempStack.append([t, i])
        return result