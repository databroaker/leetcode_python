class Solution(object):
    def defangIPaddr(self, address):
        return address.replace(".", "[.]")

print(Solution().defangIPaddr("255.100.50.0"))