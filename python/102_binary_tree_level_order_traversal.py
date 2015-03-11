# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        
        def add_to_list(l, d, p ): #l:list, d:deep
            if len(l) <= d:
                l.append([])
            l[d].append(p.val)
            if p.left:
                add_to_list(l, d+1, p.left)
            if p.right:
                add_to_list(l, d+1, p.right)

        l = []
        if not root:
            return l
        add_to_list(l, 0, root)
        return l

# Accepted

