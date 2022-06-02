class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]
        len1, len2 = len(num1), len(num2)
        if len1 >= len2:
            num2 = num2 + "0" * (len1 - len2)
        else:
            num1 = num1 + "0" * (len2 - len1)

        sumStr = ""
        idx = 0
        carry = False
        while True:
            v = ord(num1[idx]) - 48 + ord(num2[idx]) - 48
            if carry:
                v = v + 1
            if v >= 10:
                v = v - 10
                carry = True
            else:
                carry = False
            sumStr = sumStr + chr(v + 48)
            idx = idx + 1
            if idx == len(num1):
                if carry:
                    sumStr = sumStr + "1"
                break

        return sumStr[::-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.addStrings("11", "123"))

    sol = Solution()
    print(sol.addStrings("456", "77"))

    sol = Solution()
    print(sol.addStrings("0", "0"))
