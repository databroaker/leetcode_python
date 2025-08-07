class Solution(object):
    def reverseString(self, s):
        p1 = 0
        p2 = len(s) - 1

        while True:
            swap = s[p1]
            s[p1] = s[p2]
            s[p2] = swap
            p1 += 1
            p2 -= 1
            if p1 >= p2:
                break

    # FASTER VERSION
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return s.reverse()

str = ["h","e","l","l","o"]
Solution().reverseString(str)
print(str)