class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        # Loop from the end to the start
        for c in reversed(s):
            value = roman[c]
            if value < prev:
                total -= value
            else:
                total += value
            prev = value
        return total