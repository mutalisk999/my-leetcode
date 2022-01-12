from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # type: ignore
        d: dict = dict()
        idx: int = 0
        for n in nums:
            o = target - n
            v = d.get(o)
            if v is None:
                d[n] = idx
            else:
                return [v, idx]
            idx = idx + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(sol.twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print(sol.twoSum(nums, target))

