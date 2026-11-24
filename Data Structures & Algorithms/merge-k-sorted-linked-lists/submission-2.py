# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list1,list2):
            merged_list = ListNode()
            curr = merged_list

            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                else:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
            
            if list1:
                curr.next = list1
            elif list2:
                curr.next = list2
            
            return merged_list.next

        def sort_k_lists(lists, s, e):
            if len(lists) < 1:
                return 

            if s == e:
                return lists[s]
            mid = (s + e)//2

            l1 = sort_k_lists(lists, s, mid)
            l2 = sort_k_lists(lists, mid + 1, e)

            return merge_two_lists(l1, l2)


        return sort_k_lists(lists, 0, len(lists)-1)
            