class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        open = []

        for i in range(0, len(flowerbed)):
            if not flowerbed[i]:
                open.append(i)

        while n > 0:
            found_match = False
            for index in open:
                if index-1 < 0:
                    index_left = 0
                else:
                    index_left = flowerbed[index-1]

                if index+1 >= len(flowerbed):
                    index_right = 0
                else:
                    index_right = flowerbed[index+1]

                if not index_left and not index_right and not flowerbed[index]:
                    flowerbed[index] = 1
                    n -=1
                    found_match = True
                    break
            if not found_match:
                break

        return n == 0


print(Solution().canPlaceFlowers([0,0,1,0,1], 1))