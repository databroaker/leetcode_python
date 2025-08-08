class Solution(object):
    def runningSum(self, nums):
        sums = []
        if len(nums) == 0:
            return sums
        sums = [nums[0]]
        if len(nums) == 1:
            return sums
        i = 1
        while True:
            sums.append(nums[i] + sums[i-1])
            i += 1
            if i >= len(nums):
                break
        return sums

print(Solution().runningSum([1,2,3,4]))