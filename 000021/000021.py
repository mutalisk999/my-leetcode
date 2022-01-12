from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            head1, head2 = list1, list2
            if head1.val <= head2.val:
                n = ListNode(head1.val)
                headmerged = n
                head1 = head1.next
            else:
                n = ListNode(head2.val)
                headmerged = n
                head2 = head2.next
            
            while True:
                if head1 is None:
                    n.next = head2
                    return headmerged
                elif head2 is None:
                    n.next = head1
                    return headmerged
                else:
                    if head1.val <= head2.val:
                        t = ListNode(head1.val)
                        n.next = t
                        head1 = head1.next
                    else:
                        t = ListNode(head2.val)
                        n.next = t
                        head2 = head2.next
                    n = n.next
                
    
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
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(NodeToList(sol.mergeTwoLists(ListToNode(list1), ListToNode(list2))))

    list1 = []
    list2 = []
    print(NodeToList(sol.mergeTwoLists(ListToNode(list1), ListToNode(list2))))

    list1 = []
    list2 = [0]
    print(NodeToList(sol.mergeTwoLists(ListToNode(list1), ListToNode(list2))))