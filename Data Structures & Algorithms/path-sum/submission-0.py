# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []

        def backtracking(root, targetSum):
            if not root:
                return False
            
            path.append(root)
            targetSum -= root.val

            if not root.left and not root.right and targetSum == 0:
                return True
            if backtracking(root.left, targetSum):
                return True
            if backtracking(root.right, targetSum):
                return True

            targetSum += root.val
            path.pop()
            return False

        return backtracking(root, targetSum)
