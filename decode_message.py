class Solution(object):
    def decodeMessage(self, key, message):
        d = {}
        x = 'a'
        for char in key:
            if char == " ":
                continue
            if char not in d:
                d[char] = x
                x = chr(ord(x)+1)
        decoded = ""
        for m in message:
            if m != " ":
                decoded += d[m]
            else:
                decoded += " "
        return decoded

print(Solution().decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))