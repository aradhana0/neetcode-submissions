/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    ListNode prev = null;
    public ListNode reverseList(ListNode head) {
        ListNode first = recursion(head);
        return prev;
    }

    private ListNode recursion(ListNode head) {
        if (head == null || head.next == null) {
            prev = head;
            return head;
        }
        ListNode curr = recursion(head.next);
        curr.next = head;
        head.next = null;
        return head;
    }
}
