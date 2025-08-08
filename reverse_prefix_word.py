class Solution(object):
    def reversePrefix(self, word, ch):
        index = word.find(ch)
        sub = word[0:index+1][::-1]
        return sub + word[index+1:]

print(Solution().reversePrefix("abcdefd", "d"))