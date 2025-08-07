class Solution(object):
    def findWords(self, words):
        rows = [
            "qwertyuiop",
            "asdfghjkl",
            "zxcvbnm"
        ]

        new_words = []

        for word in words:
            selected_row = None
            success = True

            for letter in word:

                if not selected_row:
                    for row in rows:
                        if letter.lower() in row:
                            selected_row = row
                            break

                if letter.lower() not in selected_row:
                    success = False
                    break

            if success:
                new_words.append(word)

        return new_words



print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))