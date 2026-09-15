# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        if root:
            traversal.append([root.val])
            nodes = [root]
            i = 0
            curr = nodes[i]
            left = curr.left
            right = curr.right
            temp = []
            nodes_on = 1
            while curr:
                if curr.left:
                    temp.append(curr.left.val)
                    nodes.append(curr.left)
                if curr.right:
                    temp.append(curr.right.val)
                    nodes.append(curr.right)
                nodes_on -= 1
                if nodes_on == 0:
                    if temp:
                        traversal.append(temp)
                    temp = []
                    nodes_on = len(nodes) - (i + 1)
                i += 1
                curr = nodes[i] if i < len(nodes) else None
                if curr:
                    left = curr.left
                    right = curr.right
        return traversal
