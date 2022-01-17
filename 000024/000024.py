from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        m, n, f, pre = head, head, False, None
        while True:
            if m is None:
                return head
            n = m.next
            if n is None:
                return head
            if not f:
                head = n
                f = True

            m.next = n.next
            n.next = m
            if pre is not None:
                pre.next = n
            pre = m
            m = m.next
            

def NodeToList(l: ListNode) -> list:
    ret = list()
    while l is not None:
        ret.append(l.val)
        l = l.next
    return ret


def ListToNode(l: list) -> Optional[ListNode]:
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
    head = [1, 2, 3, 4]
    print(NodeToList(sol.swapPairs(ListToNode(head))))  # type: ignore

    head = []
    print(NodeToList(sol.swapPairs(ListToNode(head))))  # type: ignore

    head = [1]
    print(NodeToList(sol.swapPairs(ListToNode(head))))  # type: ignore
