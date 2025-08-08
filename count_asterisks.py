class Solution(object):
    def countAsterisks(self, s):
        bar = 0
        c = 0
        for char in s:
            if not bar:
                if char == "*":
                    c += 1
            if char == "|":
                bar = (bar + 1) % 2
        return c

print(Solution().countAsterisks("l|*e*et|c**o|*de|"))