class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nextNode, cnt = head, 0
        while nextNode is not None:
            nextNode = nextNode.next
            cnt = cnt + 1
        m = cnt - n
        if m == 0:
            return head.next
        
        nextNode = head
        for i in range(m - 1):
            nextNode = nextNode.next
        nextNode.next = nextNode.next.next
        return head


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
    head = [1, 2, 3, 4, 5]
    n = 2
    l = ListToNode(head)
    print(NodeToList(sol.removeNthFromEnd(l, n)))
    
    head = [1]
    n = 1
    l = ListToNode(head)
    print(NodeToList(sol.removeNthFromEnd(l, n)))
    
    head = [1, 2]
    n = 1
    l = ListToNode(head)
    print(NodeToList(sol.removeNthFromEnd(l, n)))
