import unittest
from tests.sprint1_acceptance_test.sprint1_acceptance_test import acceptanceTest
from admin_create_account import TestAdmCreateAccount
from admin_delete_account import TestAdmDeleteAccount
from admin_edit_account import TestAdminEditAccount
from admin_send_notifications import TestAdminNotify
from admin_show_information import TestAdminInfo
from instructor_access_info import TestInsAccessInfo
from instructor_assign_TA_lab import InstructAssignTALab

from instructor_edit_info import TestInstructEdit
from instructor_view_assignments import TestInstructorViewAssignments
from More_acceptance_tests import TestSupCreateAccount
from supervisor_assign_lab import TestSupAssignTALab
from supervisor_assign_TA_lab import TestSignTALab
from supervisor_assign_TAs_course import TestSupAssignCourse
from supervisor_create_account import TestSupCreateAccount2
from supervisor_create_course import TestSupCreateCourse
from supervisor_delete_account import TestSupDelAccount
from supervisor_edit_account import TestSupEditAccount
from supervisor_send_notification import TestSupNotify
from supervisor_show_TA import TestSupShow
from TA_access_info import TestTAAccessInfo
from TA_edit_info import TestTAInfo
from TA_view_assignments import TestTAViewAssignments

def main_tests():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(acceptanceTest))
    suite.addTest(unittest.makeSuite(TestAdmCreateAccount))
    suite.addTest(unittest.makeSuite(TestAdmDeleteAccount))
    suite.addTest(unittest.makeSuite(TestAdminEditAccount))
    suite.addTest(unittest.makeSuite(TestAdminEditAccount))
    suite.addTest(unittest.makeSuite(TestAdminNotify))
    suite.addTest(unittest.makeSuite(TestAdminInfo))

    suite.addTest(unittest.makeSuite(TestInsAccessInfo))
    suite.addTest(unittest.makeSuite(InstructAssignTALab))

    # suite.addTest(unittest.makeSuite(TestInstructEdit)) CONCATENATE ISSUE
    # suite.addTest(unittest.makeSuite(TestInstructorViewAssignments)) NO VIEW ASSIGNMENT COMMAND

    # suite.addTest(unittest.makeSuite(TestSupCreateAccount)) (MORE ACCEPTANCE TESTS)

    suite.addTest(unittest.makeSuite(TestSupAssignTALab))
    suite.addTest(unittest.makeSuite(TestSignTALab))
    suite.addTest(unittest.makeSuite(TestSupAssignCourse))        # 'NoneType' object has no attribute 'getRole'
    suite.addTest(unittest.makeSuite(TestSupCreateAccount2))
    suite.addTest(unittest.makeSuite(TestSupCreateCourse))
    suite.addTest(unittest.makeSuite(TestSupDelAccount))
    suite.addTest(unittest.makeSuite(TestSupEditAccount))
    suite.addTest(unittest.makeSuite(TestSupNotify))              # No command for notify
    # suite.addTest(unittest.makeSuite(TestSupShow))                CONCATENATE ISSUE
    # suite.addTest(unittest.makeSuite(TestTAAccessInfo))           NO VIEW ASSIGNMENT COMMAND
    # suite.addTest(unittest.makeSuite(TestTAInfo))               # NO VIEW ASSIGNMENT COMMAND
    # suite.addTest(unittest.makeSuite(TestTAViewAssignments))    # NO VIEW ASSIGNMENT COMMAND


    runner = unittest.TextTestRunner()
    res=runner.run(suite)
    print(res)
