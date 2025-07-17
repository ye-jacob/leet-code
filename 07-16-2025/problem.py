class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        print(words)
        reverse = ''
        while len(words) > 1:
            reverse += words.pop() + ' '
        return reverse + words.pop()


print(Solution().reverseWords("Let's take LeetCode contest"))




