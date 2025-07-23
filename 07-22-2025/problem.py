class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        for i in range(0, len(str(x))):
            if x[i] != x[len(x)-i-1]:
                return False
        return True
        