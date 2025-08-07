from pprint import pprint


class Solution(object):
    def firstUniqChar(self, s):
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] = d[char] + 1
        for i in range(0, len(s)):
            char = s[i]
            if d[char] == 1:
                return i
        return -1


print(Solution().firstUniqChar("loveleetcode"))