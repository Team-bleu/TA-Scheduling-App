import unittest
from application.tests.sprint1_acceptance_test.sprint1_acceptance_test import acceptanceTest



def main_tests():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(acceptanceTest))

    runner = unittest.TextTestRunner()
    res=runner.run(suite)
    print(res)
