class Solution(object):
    def reverseDegree(self, s):
        return sum([abs(ord(s[i])-96-27)*(i+1) for i in range(0, len(s))])

print(Solution().reverseDegree("abc"))