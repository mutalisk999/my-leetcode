class Solution:
    def isValid(self, s: str) -> bool:
        li = list()
        d = {'(': ')', '{': '}', '[': ']'}
        d2 = {')': '(', '}': '{', ']': '['}
        for c in s:
            if len(li) == 0:
                if c in ")]}":
                    return False
                else:
                    li.append(c)
            else:
                if c in ")]}":
                    if d2.get(c) not in li:
                        return False
                    if d.get(li[-1]) == c:
                        li.pop()
                elif c in "([{":
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
