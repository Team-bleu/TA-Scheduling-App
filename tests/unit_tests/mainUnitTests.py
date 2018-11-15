import unittest
from AddCommandTest import AddCommandTest
from AssignCourseCommandTest import AssignCourseCommandTest
from AssignLabCommandTest import AssignLabCommandTest
from CreateCourseTest import CreateCourseTest
from CreateLabTest import CreateLabTest
from LoginCommandTest import LoginCommandTest
from LoguoutCommandTest import LogoutCommandTest
from QuitCommandTest import QuitCommandTest
from RoleCommandTest import RoleCommandTest
from ShowCommandTest import ShowCommandTest
from RemoveCommandTest import RemoveCommandTest
from UserUtilityTest import UserUtilityTest

from UserTest import UserTest



def main_tests():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(AddCommandTest))
    suite.addTest(unittest.makeSuite(CreateCourseTest))
    suite.addTest(unittest.makeSuite(CreateLabTest))
    suite.addTest(unittest.makeSuite(AssignCourseCommandTest))
    suite.addTest(unittest.makeSuite(AssignLabCommandTest))
    suite.addTest(unittest.makeSuite(LoginCommandTest))
    suite.addTest(unittest.makeSuite(UserTest))
    suite.addTest(unittest.makeSuite(UserUtilityTest))
    suite.addTest(unittest.makeSuite(QuitCommandTest))
    suite.addTest(unittest.makeSuite(RoleCommandTest))
    suite.addTest(unittest.makeSuite(ShowCommandTest))
    suite.addTest(unittest.makeSuite(RemoveCommandTest))
    suite.addTest(unittest.makeSuite(LogoutCommandTest))
    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)
