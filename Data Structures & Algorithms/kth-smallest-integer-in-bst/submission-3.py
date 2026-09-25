# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(root, k):
            if not root:
                return

            inorder(root.left, k-1)
            result.append(root.val)
            # if k == 0:
            #     break
            inorder(root.right, k-1)

        inorder(root, k)

        return result[k-1]