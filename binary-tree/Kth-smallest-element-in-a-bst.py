# Definition for a binary tree node.
from typing import Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        answer = 0
        def helper(root):
            nonlocal count, answer
            if not root:
                return

            helper(root.left)
            count +=1
            if count == k:
                answer = root.val
            helper(root.right)
            
            
            
        helper(root)
        return answer