class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max = 0
        for i in range(0, len(s)):
            tmp = ""
            for ii in range(i, len(s)):
                if s[ii] not in tmp:
                    tmp += s[ii]
                else:
                    break
            if len(tmp) > max:
                max = len(tmp)
        return max

print(Solution().lengthOfLongestSubstring("pwwkew"))