class Solution(object):
    def reverse(self, x):
        rev_x = str(x)[::-1]
        sign = 1
        if "-" in rev_x:
            rev_x = rev_x.replace("-", "")
            sign = -1

        rev_x = int(rev_x)

        if rev_x > 2 ** 31 - 1:
            return 0
        else:
            return rev_x * sign

print(Solution().reverse(-123))