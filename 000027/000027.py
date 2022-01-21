from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, p = len(nums), 0
        for i in range(l):
            if nums[i] == val:
                continue
            else:
                nums[p] = nums[i]
                p = p + 1
        return p


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    v = sol.removeElement(nums, val)
    print(v, ", nums = ", nums[0:v])
    
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    v = sol.removeElement(nums, val)
    print(v, ", nums = ", nums[0:v])

