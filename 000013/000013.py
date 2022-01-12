class Solution:
    def romanToInt(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        lac, sum = 0, 0
        for i in range(len(s)-1, -1, -1):
            v = m[s[i]]
            if v < lac:
                sum = sum - v
            else:
                sum = sum + v
            lac = v
        return sum
        

if __name__ == "__main__":
    sol = Solution()
    s = "III"
    print(sol.romanToInt(s))

    s = "IV"
    print(sol.romanToInt(s))

    s = "IX"
    print(sol.romanToInt(s))

    s = "LVIII"
    print(sol.romanToInt(s))

    s = "MCMXCIV"
    print(sol.romanToInt(s))
