from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx1, idx2, len1, len2 = 0, 0, len(nums1), len(nums2)
        mid1, mid2, cnt = 0, 0, 0
        mid1v = 0

        lentotal = len1 + len2
        if lentotal & 0x1 == 0x1:
            mid1 = lentotal // 2
        else:
            mid2 = lentotal // 2
            mid1 = mid2 - 1

        while True:
            v = 0

            if idx1 >= len1 or idx2 >= len2:
                if idx1 >= len1:
                    v = nums2[idx2]
                    idx2 = idx2 + 1
                elif idx2 >= len2:
                    v = nums1[idx1]
                    idx1 = idx1 + 1
            else:
                if nums1[idx1] >= nums2[idx2]:
                    v = nums2[idx2]
                    idx2 = idx2 + 1
                else:
                    v = nums1[idx1]
                    idx1 = idx1 + 1

            if lentotal & 0x1 == 0x1:
                if cnt == mid1:
                    return float(v)
            else:
                if cnt == mid1:
                    mid1v = v
                elif cnt == mid2:
                    return float((mid1v + v) / 2)

            cnt = cnt + 1


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(sol.findMedianSortedArrays(nums1, nums2))

    nums1 = [0, 0]
    nums2 = [0, 0]
    print(sol.findMedianSortedArrays(nums1, nums2))

    nums1 = []
    nums2 = [1]
    print(sol.findMedianSortedArrays(nums1, nums2))

    nums1 = [2]
    nums2 = []
    print(sol.findMedianSortedArrays(nums1, nums2))
