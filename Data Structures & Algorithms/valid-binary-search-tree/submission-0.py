# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       return self.isbst(root,-float('inf'),float('inf'))
    def isbst(self,node,low,high):
        if(node==None):
            return True
        if(not((low<node.val)and(high>node.val))):
            return False
        return (self.isbst(node.left,low,node.val))and(self.isbst(node.right,node.val,high))
        

        