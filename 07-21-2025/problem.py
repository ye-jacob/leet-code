class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1

        longest = ''
        for i in range(len(s)):
            # print("longest:" + longest)
            # start with i = 0
            longest_ = ''
            # print("longest_" + longest_)
            for j in range(i, len(s)):
                if s[j] not in longest_:
                    longest_ += s[j]
                else:
                    break
                # print(str(i) + ' ' + str(j) + ' ' + longest_ + ' ' + s[j])
                if len(longest_) > len(longest):
                        longest = longest_
                
                
                
            #checks if current greater than longest
        return len(longest)
