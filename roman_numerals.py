# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution(object):
    def romanToInt(self, s):
        mapping = {"I" : 1, "V": 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000,
                   "IV": 4, "IX": 9,
                   "XL": 40, "XC": 90,
                   "CD": 400, "CM": 900}

        total = 0
        last = 0

        s = s[::-1]
        i = 0
        while True:
            char = s[i]

            try:
                new_combo = (char + s[i+1])[::-1]
                amt = mapping[new_combo]
                i += 1
            except:
                amt = mapping[char]

            total += amt

            i += 1
            if i >= len(s):
                break



        return total

    # Faster Solution
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):
            curr_value = roman_map[char]
            if curr_value < prev_value:
                total -= curr_value
            else:
                total += curr_value
                prev_value = curr_value

        return total

print(Solution().romanToInt("MCMXCIV")) #1994