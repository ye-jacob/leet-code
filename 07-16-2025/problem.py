class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        print(words)
        reverse = ''
        while len(words) > 0:
            reverse += words.pop() + ' '
        return reverse 


print(Solution().reverseWords("Let's take LeetCode contest"))




