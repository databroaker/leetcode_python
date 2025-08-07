class Solution(object):
    def balancedStringSplit(self, s):
        s1 = 0
        s2 = 1

        strings = 0

        while True:
            if s2 >= len(s):
                break
            sub = s[s1:s2+1]
            rs = sub.count("R")
            ls = sub.count("L")
            if rs == ls:
                strings += 1
                s1 = s2 + 1
                s2 = s1 + 1
            else:
                s2 += 1

        return strings


print(Solution().balancedStringSplit("LLLLRRRRL"))