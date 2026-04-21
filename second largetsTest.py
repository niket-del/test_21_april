from cmath import inf
import unittest

def secondlargest(arr):
    count1 = float('-inf')
    count2 = float('-inf')
    for ele in arr:
        if ele > count1:
            count2 = count1
            count1 = ele
        elif ele > count2 and ele != count1:
            count2 = ele
    return count2

arr = [0,0,0]
print(secondlargest(arr))


class TestSecondLargest(unittest.TestCase):
    def testNormal(self):
        self.assertEqual(secondlargest([1,4,8,4,9,5,6]), 8)
    def testZeros(self):
        self.assertEqual(secondlargest([0,0,0]), float('-inf'))
    def testNegative(self):
        self.assertEqual(secondlargest([-1,-2,-3]), -2)
    def testAll(self):
        self.assertEqual(secondlargest([-10, 1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()