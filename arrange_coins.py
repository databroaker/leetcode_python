class Solution(object):
    def arrangeCoins(self, n):
        rows = 0
        amt = 1
        while True:
            if n >= amt:
                n -= amt
                rows += 1
                amt += 1
            else:
                break
        return rows

print(Solution().arrangeCoins(3))