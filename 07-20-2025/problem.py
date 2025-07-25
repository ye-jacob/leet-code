class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()
        if len(merged) % 2 == 0:
            return (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2.0
        else:
            return merged[len(merged) // 2]

soltuion = Solution()
print(soltuion.findMedianSortedArrays([1,3], [2]))