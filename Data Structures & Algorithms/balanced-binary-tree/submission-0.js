/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {boolean}
     */
    isBalanced(root) {
        if(!root) return true; 

        const getHeight = (root) => {
            if(!root) return 0;

            return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
        }

        let left = getHeight(root.left);
        let right = getHeight(root.right);

        if(Math.abs(left - right) > 1) return false;

        return (Math.abs(left - right) <= 1 && this.isBalanced(root.left) && this.isBalanced(root.right));
    }
}
