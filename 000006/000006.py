class Solution:
    def convert(self, s: str, numRows: int) -> str:
        seq = [i for i in range(numRows)]
        seq.extend(seq[::-1][1:-1])
        slist = [""] * numRows

        for i in range(len(s)):
            idx = i % len(seq)
            row = seq[idx]
            slist[row] = slist[row] + s[i]

        return "".join(slist)


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(sol.convert(s, numRows))

    s = "PAYPALISHIRING"
    numRows = 4
    print(sol.convert(s, numRows))

    s = "A"
    numRows = 1
    print(sol.convert(s, numRows))
