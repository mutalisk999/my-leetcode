# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        retlisthead, retlistpos = None, None
        lv: int = 0
        while l1 is not None or l2 is not None:
            v1, l1 = (l1.val, l1.next) if l1 is not None else (0, None)
            v2, l2 = (l2.val, l2.next) if l2 is not None else (0, None)

            v = v1 + v2 + lv
            lv = v // 10
            node = ListNode(v % 10)

            if retlisthead is None:
                retlisthead = node
            else:
                retlistpos.next = node

            retlistpos = node

        if lv != 0:
            retlistpos.next = ListNode(lv)

        return retlisthead


def NodeToList(l: ListNode) -> list:
    ret = list()
    while l is not None:
        ret.append(l.val)
        l = l.next
    return ret


def ListToNode(l: list) -> ListNode:
    retlisthead, retlistpos = None, None
    for v in l:
        node = ListNode(v)
        if retlisthead is None:
            retlisthead = node
        else:
            retlistpos.next = node
        retlistpos = node
    return retlisthead


if __name__ == "__main__":
    sol = Solution()
    l1 = ListToNode([2, 4, 3])
    l2 = ListToNode([5, 6, 4])
    print(NodeToList(sol.addTwoNumbers(l1, l2)))

    l1 = ListToNode([0])
    l2 = ListToNode([0])
    print(NodeToList(sol.addTwoNumbers(l1, l2)))

    l1 = ListToNode([9, 9, 9, 9, 9, 9, 9])
    l2 = ListToNode([9, 9, 9, 9])
    print(NodeToList(sol.addTwoNumbers(l1, l2)))