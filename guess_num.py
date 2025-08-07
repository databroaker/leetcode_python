def guess(g):
    n = 8
    if g == n:
        return 0
    if g > n:
        return 1
    if g < n:
        return -1

class Solution(object):
    def guessNumber(self, n):
        lower = 1
        upper = n

        curr = n // 2

        while True:
            res = guess(curr)
            if res == -1: # higher
                curr = (curr + upper) // 2
            elif res == 1: # lower
                curr = (curr + lower) // 2
            elif res == 0:
                return curr

print(Solution().guessNumber(10))