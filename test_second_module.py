'''
Created on Feb 5, 2018

@author: mmp
'''
import unittest
import second_module

class Test(unittest.TestCase):


	def test_clean_sequence(self):
		
		self.assertEqual('AAACCCC', second_module.clean_fasta('aaaccccv'))

class Test1(unittest.TestCase):


	def test_clean_sequence(self):
		
		self.assertEqual('AAACCCC', second_module.clean_fasta('aaaccccv'))
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.test_clean_sequence', 'Test1.test_clean_sequence']
	unittest.main()