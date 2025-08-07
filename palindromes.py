class Solution(object):

    # Original Solution
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    # Fastest Solution
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        # Convert the number to string
        str_num = str(x)

        # Check if the number is same forwards and backwards
        return str_num == str_num[::-1]


print(Solution().isPalindrome(4324))