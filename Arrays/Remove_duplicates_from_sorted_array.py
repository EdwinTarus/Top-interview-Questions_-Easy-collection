class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # L = left pointer and R = right pointer
        # set left pointer to index 1
        L = 1
        for R in range(1, len(nums)):
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L +=1
        return L
