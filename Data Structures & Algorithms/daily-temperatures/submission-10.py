class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        tempStack = []

        for i in range(len(temperatures)):
            while tempStack and temperatures[i] > temperatures[tempStack[-1]]:
                idx = tempStack.pop()
                result[idx] = i - idx
            tempStack.append(i)

        return result