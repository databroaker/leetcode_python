class Solution(object):
    def findTheDifference(self, s, t):
        for char in s:
            t = t.replace(char, "", 1)
        return t

print(Solution().findTheDifference("abcd", "abcde"))