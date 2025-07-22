class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two sorted arrays
        merged = nums1 + nums2
        merged.sort()
        
        # Find the median
        n = len(merged)
        if n % 2 == 0:
            # Even length: average of two middle elements
            return (merged[n//2 - 1] + merged[n//2]) / 2.0
        else:
            # Odd length: middle element
            return float(merged[n//2])


# Test the solution
solution = Solution()
print(solution.findMedianSortedArrays([1, 3], [2]))  # Expected: 2.0
print(solution.findMedianSortedArrays([1, 2], [3, 4]))  # Expected: 2.5




