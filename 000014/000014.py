from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0

        while True:
            c = None
            for s in strs:
                if idx >= len(s):
                    return s[:idx]
                if c is None:
                    c = s[idx]
                elif c != s[idx]:
                    return s[:idx]

            idx = idx + 1


if __name__ == "__main__":
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    print(sol.longestCommonPrefix(strs))

    strs = ["dog", "racecar", "car"]
    print(sol.longestCommonPrefix(strs))

