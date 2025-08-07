class Solution(object):
    def reverseVowels(self, s):
        p1 = 0
        p2 = len(s) - 1
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        s = list(s)
        while True:
            if s[p1] in vowels and s[p2] in vowels:
                s[p1], s[p2] = s[p2], s[p1]
                p1 +=1
                p2 -= 1
            else:
                if s[p1] not in vowels:
                    p1 += 1
                if s[p2] not in vowels:
                    p2 -= 1

            if p1 >= p2:
                break

        return "".join(s)


print(Solution().reverseVowels("leetcode"))