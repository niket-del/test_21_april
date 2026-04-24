import unittest



class FebbonacciTest(unittest.TestCase):
    def testFeb(self):
        self.assertEqual(Febonacci(5),[0,1,1,2,3])


if __name__ == "__main__":
    unittest.main()