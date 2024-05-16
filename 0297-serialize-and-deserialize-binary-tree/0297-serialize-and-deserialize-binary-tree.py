# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        res = []
        
        def dfs(node): # preorder traversal (root,left,right)
            if node is None:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        nodes = data.split(',')
        self.i = 0
        
        def dfs():
            if nodes[self.i] == 'N':
                self.i = self.i + 1
                return None
            node = TreeNode(nodes[self.i])
            self.i = self.i + 1
        
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))