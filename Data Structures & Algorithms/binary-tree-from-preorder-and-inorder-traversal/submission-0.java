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
    public TreeNode buildTree(int[] pre, int[] in) {
        Map<Integer, Integer> map = new HashMap<>();
        for(int i=0; i<in.length; i++) map.put(in[i], i);
        return helper(pre, new int[1], 0, pre.length-1, map);
    }

    private TreeNode helper(int[] pre, int[] index, int left, int right, Map<Integer, Integer> map) {
        if (left>right) return null;
        int rootValue = pre[index[0]++];
        TreeNode root = new TreeNode(rootValue);
        root.left = helper(pre, index, left, map.get(rootValue)-1, map);
        root.right = helper(pre, index, map.get(rootValue)+1, right, map);
        return root;
    }
}
