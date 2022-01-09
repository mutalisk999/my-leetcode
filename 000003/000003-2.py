class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxS, idxE, substrlenMax, strlen = 0, 0, 0, len(s)

        while True:
            d = dict()
            while True:
                if idxE >= strlen:
                    break
                if s[idxE] not in d:
                    d[s[idxE]] = idxE
                else:
                    break
                idxE = idxE + 1

            l = idxE - idxS
            if l > substrlenMax:
                substrlenMax = l

            if idxE >= strlen:
                return substrlenMax

            if s[idxE] in d:
                idxS = d[s[idxE]] + 1
                idxE = idxS


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
    print(sol.lengthOfLongestSubstring(" "))