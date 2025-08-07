class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))