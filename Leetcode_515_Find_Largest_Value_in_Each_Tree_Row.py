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
        row = [2,1,3,6,5,4,7]
        root = TreeSolution().AddTreeNode(row)
        self.assertEqual(Solution().largestValues(root),[2,3,7]);
    def testAnotherCase(self):
        row = [1,3,2,5,3,None,9]
        root = TreeSolution().AddTreeNode(row)
        self.assertEqual(Solution().largestValues(root),[1,3,9]);
class TreeSolution(object):
    def AddTreeNode(self,row):
        if not row:
            return None
        i = 0
        root = TreeNode(row[i])
        i = i+1
        queue = [root]
        for node in queue:
            if i < len(row):
                node.left = TreeNode(row[i])
                i = i+1
            if i < len(row):
                node.right = TreeNode(row[i])
                i = i+1
            queue += filter(None, (node.left,node.right))
        return root
class Solution(object):
    def maxFunc(self,a,b):
        if a is None:
            return b
        elif b is None:
            return a
        else:
            return max(a,b)
    def largestValues(self, root):
        if not root:
            return []
        left = self.largestValues(root.left)
        right = self.largestValues(root.right)
        return [root.val] + list(map(self.maxFunc, left, right))  

if __name__ == '__main__':
    unittest.main()
