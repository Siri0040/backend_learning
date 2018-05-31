import unittest

class MyFirstTests(unittest.TestCase):
	def test_hello(self):
		self.assertEqual(hello_world(), 'hello world')

def hello_world():
	return 'hello world'	
		
if __name__ == '__main__':
	unittest.main()