from pprint import pprint


class Solution(object):
    def wordPattern(self, pattern, s):
        d = dict()
        ss = s.split()

        for p in pattern:
            if p not in d:
                try:
                    d[p] = ss[0]
                except:
                    return False
                while d[p] in ss:
                    ss.remove(d[p])

        d = {value: key for key, value in d.items()}

        sss = list(set(s.split()))
        s = s.split()
        switches = []
        for word in sss:
            if word not in d:
                return False
            match = d[word]
            for i in range(0, len(s)):
                if s[i] == word and i not in switches:
                    s[i] = match
                    switches.append(i)
        return "".join(s) == pattern

print(Solution().wordPattern("abc", "b c a"))