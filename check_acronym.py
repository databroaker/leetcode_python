class Solution(object):
    def isAcronym(self, words, s):
        return "".join([word[0] for word in words]) == s

print(Solution().isAcronym(["alice","bob","charlie"], "abc"))