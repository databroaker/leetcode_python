class Solution(object):
    def differenceOfSums(self, n, m):
        num1 = 0
        num2 = 0

        for i in range(1, n+1):
            divisble = i % m
            if not divisble:
                num2 += i
            else:
                num1 += i

        return num1 - num2

print(Solution().differenceOfSums(10, 3))