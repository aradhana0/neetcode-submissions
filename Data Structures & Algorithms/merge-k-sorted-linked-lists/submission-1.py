# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            result = ListNode()
            curr = result

            while l1 and l2:
                if l1.val <= l2.val:
                    temp = l1
                    l1 = l1.next
                    curr.next = temp
                    curr = curr.next
                else:
                    temp = l2
                    l2 = l2.next
                    curr.next = temp
                    curr = curr.next

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2

            return result.next


        def sortKLists(lists, l, r):
            
            mid = (r + l)//2

            if l == r:
                return lists[l];

            l1 = sortKLists(lists,l, mid)
            l2 = sortKLists(lists, mid+1, r)


            return mergeTwoLists(l1,l2)

        if len(lists) < 1:
            return
        return sortKLists(lists, 0, len(lists) - 1)
            