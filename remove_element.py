class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        for num in list(nums):
            if num == val:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)

print(Solution().removeElement([3,2,2,3], 3))