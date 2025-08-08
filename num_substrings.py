class Solution(object):
    def numOfStrings(self, patterns, word):
        c = 0
        for p in patterns:
            if p in word: c += 1
        return c

print(Solution().numOfStrings(["a","abc","bc","d"], "abc"))