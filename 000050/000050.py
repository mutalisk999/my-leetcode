#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n > 0:
            isPos = True
        else:
            isPos = False
            n = -n

        def binExpMax(n):
            if n == 0 or n == 1:
                return n
            m = 1
            while m * 2 <= n:
                m = m * 2
            return m

        l = list()
        while n > 0:
            maxExp = binExpMax(n)
            l.append(maxExp)
            n = n - maxExp

        cached = {1: x}
        cnt = 2
        while cnt <= max(l):
            cached[cnt] = cached[cnt // 2] * cached[cnt // 2]
            cnt = cnt * 2

        val = 1.0
        for i in l:
            val = val * cached[i]

        if isPos:
            return val
        else:
            return 1.0 / val


if __name__ == "__main__":
    sol = Solution()
    x = 2.00000
    n = 10
    print(sol.myPow(x, n))

    x = 2.10000
    n = 3
    print(sol.myPow(x, n))

    x = 2.00000
    n = -2
    print(sol.myPow(x, n))
