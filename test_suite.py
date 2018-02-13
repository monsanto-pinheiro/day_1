'''
Created on Feb 5, 2018

@author: mmp
'''
import unittest
import test_second_second
import test_second_module

if __name__ == '__main__':
	suite=unittest.TestSuite()
	suite.addTests([test_second_second.Test2("test_xpro"), test_second_module.Test("test_clean_sequence")])
	suite.addTests([test_second_second.Test2(), test_second_module.Test()])
	runner = unittest.TextTestRunner()
	runner.run (suite)
	