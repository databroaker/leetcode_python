class Solution(object):
    def searchInsert(self, nums, target):
        prev = nums[0]
        if target == prev:
            return 0
        for i in range(1, len(nums)):
            n = nums[i]
            if n == target:
                return i
            if prev < target < n:
                return i
        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

print(Solution().searchInsert([1,3,5,6], 5))