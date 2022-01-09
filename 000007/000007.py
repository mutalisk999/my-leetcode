class Solution:
    def reverse(self, x: int) -> int:
        n = -1 if x < 0 else 1
        x = -x if n == -1 else x

        y = 0
        while x >= 10:
            y = y * 10 + (x % 10)
            x = x // 10
        res = n * (y * 10 + x)

        if res < ((-1) * (1 << 31)) or res > ((1 << 31) - 1):
            return 0
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(123))
    print(sol.reverse(-123))
    print(sol.reverse(120))
    print(sol.reverse(1534236469))
    print(sol.reverse(1563847412))
