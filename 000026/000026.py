from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, p = len(nums), 0
        for i in range(l):
            if nums[p] == nums[i]:
                continue
            else:
                p = p + 1
                nums[p] = nums[i]
        return p + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2]
    v = sol.removeDuplicates(nums)
    print(v, ", nums = ", nums[0:v])
    
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    v = sol.removeDuplicates(nums)
    print(v, ", nums = ", nums[0:v])
