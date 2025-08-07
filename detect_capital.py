class Solution(object):
    def detectCapitalUse(self, word):
        upper = word.upper()
        lower = word.lower()

        if word == upper or word == lower:
            return True

        if word[0] == upper[0] and word[1:] == lower[1:]:
            return True

        return False

print(Solution().detectCapitalUse("JeetcoDe"))