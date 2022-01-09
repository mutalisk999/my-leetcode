from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx1, idx2, len1, len2 = 0, 0, len(nums1), len(nums2)
        merged = list()
        while True:
            if idx1 >= len1:
                merged.extend(nums2[idx2:])
                break
            elif idx2 >= len2:
                merged.extend(nums1[idx1:])
                break
            if nums1[idx1] < nums2[idx2]:
                merged.append(nums1[idx1])
                idx1 = idx1 + 1
            else:
                merged.append(nums2[idx2])
                idx2 = idx2 + 1
        mlen = len(merged)
        if mlen & 0x1 == 0x1:
            return float(merged[mlen//2])
        else:
            return float((merged[mlen//2] + merged[mlen//2 - 1]) / 2)


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
