class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1[:] = nums1[:m]
        nums2[:] = nums2[:n]
        nums1.extend(nums2)
        nums1.sort()
        while 0 in nums1:
            nums1.remove(0)
        print(nums1)



print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))