class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
           if word == word[::-1]:
               return word
        return ""

print(Solution().firstPalindrome(["abc","car","ada","racecar","cool"]))