import unittest,os, sys
from unittest.mock import patch,Mock

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
grandParent = os.path.dirname(parent)
sys.path.append(parent)
from controller.utils.DataHandler import (
    analyzer,
    percentageCalculator
)

class TestDataHandler(unittest.TestCase):

    def testPercentageCalculator(self):
        self.assertEqual(percentageCalculator(5,10), 50.00) 
    
    def testAnalyzerIntegration(self):
        res = analyzer()
        self.assertTrue(isinstance(res,dict))


