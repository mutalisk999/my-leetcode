class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxS, idxE, substrlenMax, strlen = 0, 0, 0, len(s)
        d = dict()

        while True:
            if idxE >= strlen:
                return idxE - idxS if idxE - idxS > substrlenMax else substrlenMax

            if s[idxE] not in d:
                d[s[idxE]] = idxE
                idxE = idxE + 1
            else:
                substrlenMax = idxE - idxS if idxE - idxS > substrlenMax else substrlenMax
                idxS = d[s[idxE]] + 1
                idxE = idxS
                d = dict()


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))
    print(sol.lengthOfLongestSubstring(" "))
