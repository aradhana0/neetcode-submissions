# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        if not root:
            return True
        
        
        def checkValidity(curr):
            if not curr:
                return True
            leftTreeHeight = height(curr.left)
            rightTreeHeight = height(curr.right)
            
            if abs(leftTreeHeight - rightTreeHeight) > 1:
                return False

            left = checkValidity(curr.left)
            right = checkValidity(curr.right)

            return left == True and right == True

        return checkValidity(root)
            