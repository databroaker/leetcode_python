class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        n = 0

        for char in stones:
            if char in jewels:
                n += 1

        return n

print(Solution().numJewelsInStones("aA", "aAAbbbb"))