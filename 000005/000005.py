class Solution:
    def longestPalindrome(self, s: str) -> str:  # type: ignore
        sl = len(s)
        for i in range(sl):
            for j in range(0, i+1):
                t = s[j: j+sl-i]
                
                #
                if t == t[::-1]:
                    return t
                
                #
                # lt, f = len(t), True
                # for m in range(lt // 2):
                #     if t[m] != t[lt-1-m]:
                #         f = False
                #         break
                # if f:
                #     return t
                    

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

