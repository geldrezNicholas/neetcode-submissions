# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        array = []

        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            array.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1, len(array)):
            if array[i] <= array[i-1]:
                return False
        
        return True