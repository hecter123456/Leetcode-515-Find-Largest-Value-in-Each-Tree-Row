import unittest
from collections import deque

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNone(self):
        root = None
        self.assertEqual(Solution().largestValues(root),[]);
    def testThirdLevelTree(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(4)
        root.left.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().largestValues(root),[2,3,7]);
class Solution(object):
    def largestValues(self, root):
        ans = []
        if root is None:
            return ans
        q = [root]
        level = deque([0])
        for node in q:
            num = level.popleft()
            if len(ans) == num:
                ans.append(node.val)
            else:
                ans[num] = max(node.val,ans[num])
            if node.right is not None:
                level.append(num+1)
            if node.left is not None:
                level.append(num+1)
            q += (filter(None, (node.right,node.left)))
        return ans

if __name__ == '__main__':
    unittest.main()
