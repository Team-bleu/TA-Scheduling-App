import unittest
from supervisor_assign_lab import TestSupAssignTALab
from supervisor_create_account import TestSupCreateAccount
from supervisor_assign_TAs_course import TestSupAssignCourse
from supervisor_delete_account import TestSupDelAccount
from supervisor_assign_TA_lab import TestSignTALab
from supervisor_create_course import TestSupCreateCourse
from supervisor_show_TA import TestSupShow
from supervisor_edit_account import TestSupEditAccount
from supervisor_login_logout import TestSupLoginLogout
from supervisor_send_notification import TestSupNotify
from admin_create_account import TestAdmCreateAccount
from admin_delete_account import TestAdmDeleteAccount
from admin_edit_account import TestAdminEditAccount
from admin_send_notifications import TestAdminNotify
from instructor_access_info import TestInsAccessInfo
from instructor_edit_info import TestInstructEdit
from instructor_view_assignments import TestInstructorViewAssignments
from instructor_assign_TA_lab import InstructAssignTALab
from admin_show_information import TestAdminInfo
from TA_edit_info import TestTAInfo
from TA_access_info import TestTAAcessInfo
from TA_view_assignments import TestTAViewAssignments

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSupAssignTALab))
suite.addTest(unittest.makeSuite(TestSupCreateAccount))
suite.addTest(unittest.makeSuite(TestSupCreateAccount))
suite.addTest(unittest.makeSuite(TestAdmDeleteAccount))
suite.addTest(unittest.makeSuite(TestAdminEditAccount))
suite.addTest(unittest.makeSuite(TestAdminNotify))
suite.addTest(unittest.makeSuite(TestInsAccessInfo))
suite.addTest(unittest.makeSuite(TestInstructEdit))
suite.addTest(unittest.makeSuite(TestInstructorViewAssignments))
suite.addTest(unittest.makeSuite(TestAdminInfo))
suite.addTest(unittest.makeSuite(TestSupAssignCourse))
suite.addTest(unittest.makeSuite(TestSupDelAccount))
suite.addTest(unittest.makeSuite(TestTAViewAssignments))
suite.addTest(unittest.makeSuite(TestTAAcessInfo))
suite.addTest(unittest.makeSuite(TestTAInfo))
suite.addTest(unittest.makeSuite(InstructAssignTALab))
suite.addTest(unittest.makeSuite(TestAdmCreateAccount))
suite.addTest(unittest.makeSuite(TestSupNotify))
suite.addTest(unittest.makeSuite(TestSupLoginLogout))
suite.addTest(unittest.makeSuite(TestSignTALab))
suite.addTest(unittest.makeSuite(TestSupCreateCourse))
suite.addTest(unittest.makeSuite(TestSupShow))
suite.addTest(unittest.makeSuite(TestSupEditAccount))



runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)