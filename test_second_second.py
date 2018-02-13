'''
Created on Feb 5, 2018

@author: mmp
'''
import unittest
import second_module

class Test2(unittest.TestCase):


	def test_xpro(self):
		self.assertEqual('AAACCCC', second_module.clean_fasta('aaaccccv'))


if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test2.test_xpro']
	unittest.main()