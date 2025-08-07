class Solution(object):
    def addBinary(self, a, b):

        a = a[::-1]
        b = b[::-1]

        if len(a) > len(b):
            n1 = a
            n2 = b
        else:
            n1 = b
            n2 = a

        i = 0
        carry = 0
        result = []
        for t1 in n1:
            try:
                t2 = n2[i]
            except:
                t2 = "0"
            ones = [t1, t2, carry].count("1")
            if ones == 3:
                carry = "1"
                result.append("1")
            if ones == 2:
                carry = "1"
                result.append("0")
            if ones == 1:
                carry = "0"
                result.append("1")
            if ones == 0:
                carry = "0"
                result.append("0")

            i += 1
        if carry == "1":
            result.append(carry)
        result.reverse()
        return "".join(result)


print(Solution().addBinary("1111", "1111"))