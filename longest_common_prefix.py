class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        prefix = ""
        while True:
            l = []
            for str in strs:
                try:
                    l.append(str[i])
                except:
                    l.append("")
                    pass
            if len(set(l)) == 1 and l[0] != "":
                prefix += l[0]
            else:
                break
            i += 1
        return prefix

    # FASTER
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        f = strs[0]
        l = strs[-1]
        r = []
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                break
            r.append(f[i])
        return ''.join(r)

print(Solution().longestCommonPrefix(["flower","flow","flight"]))