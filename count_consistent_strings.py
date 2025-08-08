class Solution(object):
    def countConsistentStrings(self, allowed, words):
        good_words = 0
        for word in words:
            good = True
            for char in word:
                if char not in allowed:
                    good = False
                    break
            if good:
                good_words += 1
        return good_words

print(Solution().countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))