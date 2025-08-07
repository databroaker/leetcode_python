class Solution(object):
    def plusOne(self, digits):
        strr = ""
        for d in digits: strr += str(d)
        strr = str(int(strr)+1)
        digits = []
        for s in strr: digits.append(int(s))
        return digits

print(Solution().plusOne([4,3,2,2]))