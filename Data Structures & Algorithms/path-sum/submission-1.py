# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def targetPath(root, target):

            if not root:
                return False

            target -= root.val

            if target == 0 and not root.left and not root.right:
                return True
            if targetPath(root.left, target):
                return True
            if targetPath(root.right, target):
                return True

            return False

        return targetPath(root, targetSum)
                
            
