from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        origin = [first]
        for i in encoded:
            first = first ^ i
            origin.append(first)
        return origin


if __name__ == "__main__":
    sol = Solution()
    encoded = [1, 2, 3]
    first = 1
    print(sol.decode(encoded, first))

    sol = Solution()
    encoded = [6, 2, 7, 3]
    first = 4
    print(sol.decode(encoded, first))
