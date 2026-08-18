# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        if not root:
            return stack
        self.inorder(root, stack)
        return stack
        
    def inorder(self, root: Optional[TreeNode], results: List[int]) -> None:
        if not root:
            return
        self.inorder(root.left, results)
        results.append(root.val)
        self.inorder(root.right, results)
