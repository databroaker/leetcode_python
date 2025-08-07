class Solution(object):
    def convert_to_int(self, num):
        ords = [ord(c) for c in num]
        digits = []
        for n in ords:
            digits.append(n-48)
        digits.reverse()
        return digits

    def convert_to_string(self, num_list):
        res = ""
        for num in num_list:
            res += str(chr(num+48))
        return res

    def addStrings(self, num1, num2):
        n1 = self.convert_to_int(num1)
        n2 = self.convert_to_int(num2)

        max_len = max(len(n1), len(n2))

        res_list = []

        carry = 0
        for i in range(0, max_len):
            try:
                dig1 = n1[i]
            except:
                dig1 = 0
            try:
                dig2 = n2[i]
            except:
                dig2 = 0

            res = dig1 + dig2 + carry

            if res >= 10:
                carry = 1
                res -= 10
            else:
                carry = 0

            res_list.append(res)

        if carry:
            res_list.append(1)
        res_list.reverse()
        return self.convert_to_string(res_list)

print(Solution().addStrings("1", "9"))