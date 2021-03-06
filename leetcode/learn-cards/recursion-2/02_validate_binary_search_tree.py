class Solution:
    def isValidBST(self, root):
        if not root: return True
        return self.helper(root)
    
    def helper(self, root, low=float('-inf'), high=float('inf')):
        if not root: return True
        
        if root.val <= low or root.val >= high:
            return False
        
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)