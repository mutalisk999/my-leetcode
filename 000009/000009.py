class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y, m = 0, x
        while m >= 10:
            y = y * 10 + (m % 10)
            m = m // 10
        r = y * 10 + m

        return True if r == x else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))
    print(sol.isPalindrome(-121))
    print(sol.isPalindrome(10))
