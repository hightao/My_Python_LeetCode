class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = []
        l1 = len(nums1)
        l2 = len(nums2)
        i1 = 0
        i2 = 0
        while i1 <= l1 - 1 and i2 <= l2 - 1:
            if nums1[i1] < nums2[i2]:
                i1, result = (i1 + 1, result + [nums1[i1]])
            else:
                i2, result = (i2 + 1, result + [nums2[i2]])
        if i1 >= l1:
            result += nums2[i2:]
        elif i2 >= l2:
            result += nums1[i1:]
        if not (l1 + l2) % 2:
            return (result[(l1 + l2) // 2] + result[(l1 + l2) // 2 - 1]) / 2
        else:
            return result[(l1 + l2) // 2]
s=Solution()
print(s.findMedianSortedArrays([2,4,5],[3,4]))
