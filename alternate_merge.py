class Solution(object):
    def mergeAlternately(self, word1, word2):
        i = 0
        j = 0

        new_string = ""
        while True:
            added = False
            if i < len(word1):
                new_string += word1[i]
                i += 1
                added = True
            if j < len(word2):
                new_string += word2[j]
                j += 1
                added = True
            if not added:
                break

        return new_string


print(Solution().mergeAlternately("abc", "pqr"))