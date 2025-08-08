class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()
            for i in range(0, len(row)):
                x = row[i]
                if x:
                    row[i] = 0
                else:
                    row[i] = 1
        return image

print(Solution().flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))