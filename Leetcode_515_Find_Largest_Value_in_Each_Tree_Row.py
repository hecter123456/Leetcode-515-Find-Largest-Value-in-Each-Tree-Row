import unittest

class TreeNode(object):
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

class unitest(unittest.TestCase):
    def testNone(self):
        root = None
        self.assertEqual(Solution().largestValues(root),None);

class Solution(object):
    def largestValues(self, root):
        if(root is None):
            return None
        return None

if __name__ == '__main__':
    unittest.main()
