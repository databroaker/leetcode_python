class Solution(object):
    def findClosest(self, x, y, z):
        abs_x = abs(z-x)
        abs_y = abs(z-y)

        dis_x = z-abs_x
        dis_y = z-abs_y

        if dis_x == dis_y:
            return 0

        if dis_x < dis_y:
            return 2
        else:
            return 1


print(Solution().findClosest(2, 7, 4))