class Solution(object):
    def checkIfPangram(self, sentence):
        letters = [chr(l) for l in range(ord('a'), ord('z')+1)]
        for char in sentence:
            if char in letters:
                letters.remove(char)
        return not letters

print(Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))