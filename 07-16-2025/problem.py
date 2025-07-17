class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        print(words)
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)

print(Solution().reverseWords("Let's take LeetCode contest"))




