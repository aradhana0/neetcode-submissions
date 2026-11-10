# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast=slow=head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = None
       
        while slow:
            curr = slow
            slow = slow.next
            curr.next = dummy
            dummy = curr

        slow2 = dummy
        slow = head
        maxTwinSum = 0
        while slow2:
            maxTwinSum = max(maxTwinSum, slow.val + slow2.val)
            slow = slow.next
            slow2 = slow2.next

        return maxTwinSum
