"""
Time Complexity : O(n)
Space Complexity : O(n)
    
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            size = len(queue)
            lis = []
            
            for i in range(size):
                cur = queue.popleft()
                lis.append(cur.val)
                
                if cur.left:
                    queue.append(cur.left)
                    
                if cur.right:
                    queue.append(cur.right)
            
            result.append(lis)
        
        return result 