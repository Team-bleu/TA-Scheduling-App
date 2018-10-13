import unittest
import assign_TA_lab_test


def main_tests():
    suite = unittest.TestSuite()

    # Add in the tests to the suite
    suite.addTest(unittest.makeSuite(assign_TA_lab_test.AssignTALab))

    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)
