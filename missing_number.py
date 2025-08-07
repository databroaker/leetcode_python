class Solution(object):
    def missingNumber(self, nums):
        original_nums = sorted(nums)
        new_nums = list(range(0, len(nums)+1))
        i = 0
        while i <= len(new_nums):
            if i >= len(nums) or original_nums[i] != new_nums[i]:
                return i
            i += 1
        return None

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        form = n * (n + 1) // 2
        return form - sum(nums)


print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))