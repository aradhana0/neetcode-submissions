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
    int val = -1;
    public int kthSmallest(TreeNode root, int k) {
        key = k;
        helper(root);
        return val;
    }

    private void helper(TreeNode root) {
        if (root == null) return;
        helper(root.left);
        if (key-- == 1) {
            val = root.val;
            return;
        }
        helper(root.right);
    }


}
