import unittest
from BrainFuck import BrainFuck

class Test(unittest.TestCase):
	def tests(self):
		# given input - expected output
		codeTestCases = [
			['#',''],
			['+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.','A'],
			['+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++..','AA'],
			['+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.+.','ABC'],
			['++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.+.','HI'],
			['+++++++++++++++++++++++++++++++++++++++++++++++++++++.-.-.-.-.','54321'],
			['++++++>++++++++++++++++++++++++++++++++++++++++++++++++.','0'],
			['>++++++<++++++++++++++++++++++++++++++++++++++++++++++++.','0'],
		]

		for i in codeTestCases:
			BF = BrainFuck(i[0])
			self.assertEqual(BF.run(), i[1])

if __name__ == '__main__':
    unittest.main()
