class Solution:
    def isValid(self, s: str) -> bool:
        li = list()
        for c in s:
            if len(li) == 0:
                if c in ")]}":
                    return False
                else:
                    li.append(c)
            else:
                c2 = li[-1]
                if (c2 == '(' and c == ')') or (c2 == '[' and c == ']') or (c2 == '{' and c == '}'):
                    li.pop()
                else:
                    li.append(c)

        return True if len(li) == 0 else False


if __name__ == "__main__":
    sol = Solution()
    s = "()"
    print(sol.isValid(s))

    s = "()[]{}"
    print(sol.isValid(s))

    s = "(]"
    print(sol.isValid(s))

    s = "(])"
    print(sol.isValid(s))
