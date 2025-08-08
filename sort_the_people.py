class Solution(object):
    def sortPeople(self, names, heights):
        d = {}
        for i in range(0, len(names)):
            d[heights[i]] = names[i]
        heights.sort(reverse=True)
        return_list = []
        for h in heights:
            return_list.append(d[h])
        return return_list

print(Solution().sortPeople(["Mary","John","Emma"], [180,165,170]))