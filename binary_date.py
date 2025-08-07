class Solution(object):
    def convertDateToBinary(self, date):
        s = date.split("-")
        for i in range(0, len(s)):
            s[i] = str(bin(int(s[i])))[2:]
        return "-".join(s)

print(Solution().convertDateToBinary("2080-02-29"))