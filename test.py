import unittest
from BrainFuck import BrainFuck

class Test(unittest.TestCase):
	def tests(self):
		codeTestCases = [
			'+>++>+++>++++'
		]

		BF = BrainFuck(8,10,codeTestCases[0])
		self.assertEqual(BF.run(), '')

if __name__ == '__main__':
    unittest.main()
