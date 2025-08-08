class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        d = {}
        for word in words:
            num = int(word[-1])
            word = word[:-1]
            d[num] = word
        return_list = []
        for i in range(1, len(words)+1):
            return_list.append(d[i])
        return " ".join(return_list)

print(Solution().sortSentence("is2 sentence4 This1 a3"))