from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        headmerged, n = None, None
        hlist = [n for n in lists if n is not None]
        
        while len(hlist) > 0:
            hlist.sort(key=lambda x: x.val)
            v = hlist[0]
 
            if headmerged is None:
                n = ListNode(v.val)
                headmerged = n
            else:
                n.next = ListNode(v.val)
                n = n.next
            
            if hlist[0].next is not None:
                hlist[0] = hlist[0].next  # type: ignore
            else:
                hlist.pop(0)
              
        return headmerged  # type: ignore


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
    lists = [ListToNode([1, 4, 5]), ListToNode([1, 3, 4]), ListToNode([2, 6])]
    print(NodeToList(sol.mergeKLists(lists)))  # type: ignore
    
    lists = []
    print(NodeToList(sol.mergeKLists(lists)))  # type: ignore

    lists = [ListToNode([])]
    print(NodeToList(sol.mergeKLists(lists)))  # type: ignore
    
