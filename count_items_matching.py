class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        rules = {
            "type": 0,
            "color": 1,
            "name": 2
        }

        matches = 0
        for item in items:
            if item[rules[ruleKey]] == ruleValue:
                matches += 1

        return matches


print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
                              "color", "silver"))