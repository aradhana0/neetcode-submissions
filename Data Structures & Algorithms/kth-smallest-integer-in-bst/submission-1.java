/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {

    int key = 0;
    public int kthSmallest(TreeNode root, int k) {
        key = k;
        return helper(root);
    }

    private int helper(TreeNode root) {
        if (root == null) return 0;
        int val = helper(root.left);
        if (key-- == 1) val = root.val;
        if (val == 0) return helper(root.right);
        else return val;
    }

    public int kthSmallest_1(TreeNode root, int k) {
        Stack<TreeNode> st = new Stack<>();
        TreeNode curr = root;
        while(curr != null || !st.isEmpty()){
            while(curr != null) {
                st.push(curr);
                curr = curr.left;
            }
            curr = st.pop();
            if (k == 1) return curr.val;
            k--;
            curr = curr.right;
        }
        return -1;
    }
}
