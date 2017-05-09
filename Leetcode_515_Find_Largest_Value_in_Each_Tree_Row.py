import unittest
import TreeSolution

class unitest(unittest.TestCase):
    def testNone(self):
        row = []
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        self.assertEqual(Solution().largestValues(root),[]);
    def testThirdLevelTree(self):
        row = [8,1,3,6,5,4,7]
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        self.assertEqual(Solution().largestValues(root),[8,3,7]);
    def testAnotherCase(self):
        row = [1,3,2,5,3,None,9]
        tree = TreeSolution.TreeSolution()
        root = tree.AddBinaryTreeNode(row)
        self.assertEqual(Solution().largestValues(root),[1,3,9]);

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        left = self.largestValues(root.left)
        right = self.largestValues(root.right)
        if left == []:
            return [root.val] + right
        elif right == []:
            return [root.val] + left
        else:
            return [root.val] + list(map(max,left, right))

if __name__ == '__main__':
    unittest.main()
