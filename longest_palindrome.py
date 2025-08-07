class Solution(object):
    def longestPalindrome(self, s):
        pairs = ""
        odds = ""

        while True:
            if len(s) <= 0:
                break
            char = s[0]
            s = s[1:]
            find = s.find(char)
            if find >= 0:
                pairs += char
                s = s[:find] + s[find+1:]
            else:
                odds += char

        return (len(pairs) * 2) + (1 if odds else 0)


print(Solution().longestPalindrome("bb"))