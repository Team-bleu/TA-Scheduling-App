import unittest
from application.tests.unit_tests.AddCommandTest import AddCommandTest
from application.tests.unit_tests.AssignCourseCommandTest import AssignCourseCommandTest
from application.tests.unit_tests.AssignLabCommandTest import AssignLabCommandTest
from application.tests.unit_tests.CreateCourseTest import CreateCourseTest
from application.tests.unit_tests.CreateLabTest import CreateLabTest
from application.tests.unit_tests.LoginCommandTest import LoginCommandTest
from application.tests.unit_tests.LoguoutCommandTest import LogoutCommandTest
from application.tests.unit_tests.QuitCommandTest import QuitCommandTest
from application.tests.unit_tests.RoleCommandTest import RoleCommandTest
from application.tests.unit_tests.ShowCommandTest import ShowCommandTest
from application.tests.unit_tests.RemoveCommandTest import RemoveCommandTest
from application.tests.unit_tests.EditCommandTest import EditCommandTest
from application.tests.unit_tests.UserUtilityTest import UserUtilityTest
from application.tests.unit_tests.UserTest import UserTest



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
    suite.addTest(unittest.makeSuite(EditCommandTest))
    suite.addTest(unittest.makeSuite(LogoutCommandTest))
    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)
