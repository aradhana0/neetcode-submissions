# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        def reverveLL(head):
            reversedHead = None

            while head:
                # print(head.val)
                curr = head
                head = head.next
                curr.next = reversedHead
                reversedHead = curr

            return reversedHead

        def mergeAlt(h1, h2):
            while h1 and h2:
                temp = h1.next
                h1.next = h2

                temp2 = h2.next
                h2.next = temp

                h1 = temp
                h2 = temp2

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr2 = slow.next
        slow.next = None

        rev = reverveLL(curr2)
        curr = head
        mergeAlt(curr, rev)
        



