class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        llength, lstr = 0, ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                v = s[i:j]
                if v == v[::-1] and len(v) > llength:
                    llength = len(v)
                    lstr = v
        return lstr


if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longestPalindrome(s))

    s = "cbbd"
    print(sol.longestPalindrome(s))

    s = "a"
    print(sol.longestPalindrome(s))

    s = "ac"
    print(sol.longestPalindrome(s))
    
    s = "bb"
    print(sol.longestPalindrome(s))

