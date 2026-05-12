class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_pointer = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[write_pointer] = nums[index]
                write_pointer += 1
        return write_pointer
        