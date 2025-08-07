class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])

print(Solution().lengthOfLastWord("   fly me   to   the moon  "))