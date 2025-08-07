class Solution(object):

    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        amt = 0
        i = 0
        for ss in s:
            if i >= len(g):
                break
            gg = g[i]
            if ss >= gg:
                amt += 1
                i += 1
        return amt



print(Solution().findContentChildren([1,2], [1,2,3]))