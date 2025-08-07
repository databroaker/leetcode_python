class Solution(object):
    def thirdMax(self, nums):
        nums = sorted(list(set(nums)))[::-1]
        return nums[2] if len(nums) >= 3 else nums[0]

print(Solution().thirdMax([1, 2]))