class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        intersection = set()
        for num in nums1:
            if self.binary_search(nums2, num):
                intersection.add(num)
        return list(intersection)
        
    def binary_search(self, arr: List[int], target: int) -> bool:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
