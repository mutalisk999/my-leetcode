class Solution:
    def myAtoi(self, s: str) -> int:
        spaceflag, isneg = True, False
        numlist = list()
        for c in s:
            if c == " ":
                if spaceflag:
                    continue
                else:
                    break
            else:
                if c == "-":
                    if spaceflag and not isneg:
                        isneg = True
                        spaceflag = False
                    else:
                        break
                elif c == "+":
                    if spaceflag:
                        spaceflag = False
                    else:
                        break
                elif c in '0123456789':
                    if spaceflag:
                        spaceflag = False
                    numlist.append(c)
                else:
                    break
        
        if len(numlist) == 0:
            return 0
        else:
            numlist = numlist[::-1]
            total = sum([(ord(numlist[i]) - ord('0')) * (10 ** i) for i in range(len(numlist))]) * (-1 if isneg else 1)
            if total < (-1) * (1 << 31):
                total = (-1) * (1 << 31)
            elif total > (1 << 31) - 1:
                total = (1 << 31) - 1
            return total


if __name__ == "__main__":
    sol = Solution()
    s = "42"
    print(sol.myAtoi(s))
    
    s = "   -42"
    print(sol.myAtoi(s))
    
    s = "4193 with words"
    print(sol.myAtoi(s))
    
    s = "words and 987"
    print(sol.myAtoi(s))
    
    s = "-91283472332"
    print(sol.myAtoi(s))

    s = "+1"
    print(sol.myAtoi(s))
    
    s = "21474836460"
    print(sol.myAtoi(s))
