import unittest

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
        q = [root]
        while any(q):
            ans.append(max(node.val for node in q))
            q = [kidnode for node in q for kidnode in (node.left, node.right) if kidnode]
        return ans

if __name__ == '__main__':
    unittest.main()
