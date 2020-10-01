import unittest
from BrainFuck import BrainFuck

class Test(unittest.TestCase):
    def tests(self):
        BF = BrainFuck(8,10,'+>++>+++>++++>')
        self.assertEqual(BF.run(), '')

if __name__ == '__main__':
    unittest.main()
