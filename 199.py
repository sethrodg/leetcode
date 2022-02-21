'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return root
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            
            l = len(queue)
            
            for i in range(l):
                node = queue.popleft()
                
                if node.left is not None: queue.append(node.left)
                if node.right is not None: queue.append(node.right)
                    
                if i == (l-1):
                    res.append(node.val)
            
        return res
        
