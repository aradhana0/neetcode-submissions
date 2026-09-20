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
     * @return {number}
     */
    diameterOfBinaryTree(root) {
        if(!root) return 0;

        let max = 0;

        const getDiameter = (root) => {
            if(!root) return 0;

            let left = getHeight(root.left);
            let right = getHeight(root.right);
  
            max = Math.max(max, left + right, getDiameter(root.left), getDiameter(root.right));
            return max;
        }

        const getHeight = (root) => {
            if(!root) return 0;

            return Math.max(getHeight(root.left), getHeight(root.right)) + 1;
        }

        return getDiameter(root);
    }
}
