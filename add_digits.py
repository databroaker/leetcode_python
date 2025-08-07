class Solution(object):
    def addDigits(self, num):
        while True:
            str_num = str(num)
            if len(str_num) <= 1:
                return num
            total = 0
            for number in str_num:
                str_number = int(number)
                total += str_number
            num = total


print(Solution().addDigits(0))