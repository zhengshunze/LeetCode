class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums
