from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while True:
            if target <= nums[s]:
                return s
            if target == nums[e]:
                return e
            if target > nums[e]:
                return e + 1
            m = (s + e) // 2
            if target == nums[m]:
                return m
            if target > nums[m]:
                s, e = m + 1, e
            else:
                s, e = s, m - 1

        
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print(sol.searchInsert(nums, target))

    nums = [1, 3, 5, 6]
    target = 2
    print(sol.searchInsert(nums, target))
    
    nums = [1, 3, 5, 6]
    target = 7
    print(sol.searchInsert(nums, target))