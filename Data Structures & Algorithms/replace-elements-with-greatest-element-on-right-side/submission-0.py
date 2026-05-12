class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_value = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for index in range(len(arr) - 2, -1, -1):
            temp = arr[index]
            arr[index] = max_value
            if temp > max_value:
                max_value = temp
        return arr