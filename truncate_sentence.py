class Solution(object):
    def truncateSentence(self, s, k):
        return " ".join(s.split()[:k])

print(Solution().truncateSentence("Hello how are you Contestant", 4))