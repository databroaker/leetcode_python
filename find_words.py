class Solution(object):
    def findWordsContaining(self, words, x):
        matches = []
        for i in range(0, len(words)):
            word = words[i]
            if x in word:
                matches.append(i)
        return matches

print(Solution().findWordsContaining(["leet","code"], "e"))