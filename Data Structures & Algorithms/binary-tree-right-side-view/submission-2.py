# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = []

        if root:
            queue.append(root)

        while len(queue) > 0:
            tempList = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tempList.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tempList[-1])

        return result
