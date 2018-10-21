import unittest
from supervisor_assign_TA_lab import SupAssignTALab



def main_tests():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite())

    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)