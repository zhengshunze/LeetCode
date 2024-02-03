class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = -1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                max_sum = max(max_sum, current_sum)
                left += 1
            else:
                right -= 1
        return max_sum
