"""
Level Order Traversal using DFS.
Time Complexity : O(n)
Space Complexity : O(n)
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = []
        
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        self.dfs(root, 0)
        return self.result 
    
    def dfs(self, root, level):
        if not root:
            return 
        
        if len(self.result) == level:
            self.result.append([])
        
        self.result[level].append(root.val)
        
        self.dfs(root.left, level + 1)
        
        self.dfs(root.right, level + 1)
            
        
        