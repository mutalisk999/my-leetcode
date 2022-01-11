class Solution:
    def intToRoman(self, num: int) -> str:
        m = (("I", "V"), ("X", "L"), ("C", "D"), ("M",))
        idx = 0
        rlist = list()
        while True:
            n = num % 10
            v = m[idx]
            if n == 0:
                pass
            elif 1 <= n <= 3:
                rlist.append(v[0] * n)
            elif n == 4:
                rlist.append(v[0]+v[1])
            elif 5 <= n <= 8:
                rlist.append(v[1]+(n-5)*v[0])
            elif n == 9:
                rlist.append(v[0]+m[idx+1][0])

            num = num // 10
            idx = idx + 1

            if num == 0:
                break

        return "".join(rlist[::-1])


if __name__ == "__main__":
    sol = Solution()
    num = 3
    print(sol.intToRoman(num))

    num = 4
    print(sol.intToRoman(num))

    num = 9
    print(sol.intToRoman(num))

    num = 58
    print(sol.intToRoman(num))

    num = 1994
    print(sol.intToRoman(num))