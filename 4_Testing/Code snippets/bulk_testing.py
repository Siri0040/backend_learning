import unittest

class SimplisticTest(unittest.TestCase):

	def test(self):
		self.failUnless(True)

class OutcomesTest(unittest.TestCase):

    def testPass(self):
        return

    def testFail(self):
        self.failIf(True)

    def testError(self):
        raise RuntimeError('Test error!')
		
class FailureMessageTest(unittest.TestCase):

    def testFail(self):
        self.failIf(True, 'failure message goes here')
		
		
if __name__ == '__main__':
	unittest.main()