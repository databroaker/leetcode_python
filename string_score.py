class Solution(object):
    def scoreOfString(self, s):
        differences = []
        previous_char = s[0]
        for char in s[1:]:
            one = ord(previous_char)
            two = ord(char)
            diff = abs(one - two)

            differences.append(diff)
            previous_char = char

        return sum(differences)

print(Solution().scoreOfString("hello"))