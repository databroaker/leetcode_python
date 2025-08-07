class Solution(object):
    def removeDuplicates(self, nums):
        s = set()
        i = 0
        while True:
            n = nums[i]
            if n in s:
                nums.pop(i)
                i -=1
            else:
                s.add(n)
            i += 1
            if i >= len(nums):
                break
        return len(nums)

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))