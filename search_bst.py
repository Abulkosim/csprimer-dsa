
class Solution(object):
    def searchBST(self, root, val):
        if root is None: 
            return None
            
        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

