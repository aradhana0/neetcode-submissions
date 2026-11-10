# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def calcLength(llist):
            curr = llist
            length = 0
            while curr:
                length += 1
                curr = curr.next

            return length

        n = calcLength(head)
        i = 0
        twinSums = []
        curr = head

        while curr:
            if i > n/2 - 1:
                idx = n - i - 1
                twinSums[idx] += curr.val
            else:
                twinSums.append(curr.val)
            i += 1
            curr = curr.next

        return max(twinSums)