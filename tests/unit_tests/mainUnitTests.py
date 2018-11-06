import unittest
from AddCommandTest import AddCommandTest
from AssignCourseCommandTest import AssignCourseCommandTest
from AssignLabCommandTest import AssignLabCommandTest
from BSTUtility_test import BSTUtilityTest
from CreateCourseTest import CreateCourseTest
from CreateLabTest import CreateLabTest
from LoginCommandTest import LoginCommandTest
from LoguoutCommandTest import LogoutCommandTest
from UserTest import UserTest



def main_tests():
    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(AddCommandTest))
    suite.addTest(unittest.makeSuite(CreateCourseTest))
    suite.addTest(unittest.makeSuite(AssignCourseCommandTest))
    suite.addTest(unittest.makeSuite(AssignLabCommandTest))
    suite.addTest(unittest.makeSuite(BSTUtilityTest))
    suite.addTest(unittest.makeSuite(CreateLabTest))
    suite.addTest(unittest.makeSuite(LoginCommandTest))
    suite.addTest(unittest.makeSuite(LogoutCommandTest))
    suite.addTest(unittest.makeSuite(UserTest))
    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)
