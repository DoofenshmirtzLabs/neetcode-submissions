class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total_len = m + n
        half = (total_len + 1) // 2

        left, right = 0, m

        while left <= right:

            acut = left + (right - left) // 2
            bcut = half - acut

            aleft = float('-inf') if acut == 0 else nums1[acut - 1]
            aright = float('inf') if acut == m else nums1[acut]

            bleft = float('-inf') if bcut == 0 else nums2[bcut - 1]
            bright = float('inf') if bcut == n else nums2[bcut]

            if aleft <= bright and bleft <= aright:

                if total_len % 2 == 1:
                    return max(aleft, bleft)

                return (
                    max(aleft, bleft)
                    + min(aright, bright)
                ) / 2

            elif aleft > bright:
                right = acut - 1

            else:
                left = acut + 1