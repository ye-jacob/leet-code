class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s)):
            if s[len(s)-1-i] == "I":
                print('adding' + str(s[len(s)-1-i]))
                sum += 1
            if s[len(s)-1-i] == "V":
                print('adding' + str(s[len(s)-1-i]))
                sum += 5
            if s[len(s)-1-i] == "X":
                print('adding' + str(s[len(s)-1-i]))
                sum += 10
            if s[len(s)-1-i] == "L":
                print('adding' + str(s[len(s)-1-i]))
                sum += 50
            if s[len(s)-1-i] == "C":
                print('adding' + str(s[len(s)-1-i]))
                sum += 100
            if s[len(s)-1-i] == "D":
                print('adding' + str(s[len(s)-1-i]))
                sum += 500
            if s[len(s)-1-i] == "M":
                print('adding' + str(s[len(s)-1-i]))
                sum += 1000
        
        return sum