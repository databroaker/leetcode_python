class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        results = []

        for i in range(0, len(candies)):
            c = candies[i]
            if c+extraCandies >= max(candies):
                results.append(True)
            else:
                results.append(False)

        return results

print(Solution().kidsWithCandies([2,3,5,1,3], 3))