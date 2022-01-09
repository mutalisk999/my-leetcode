class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))
    print(sol.climbStairs(3))


