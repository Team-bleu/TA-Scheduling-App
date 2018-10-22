import unittest
from supervisor_assign_lab import TestSupAssignTALab
from supervisor_create_account import TestSupCreateAccount
from admin_create_account import TestAdmCreateAccount
from admin_delete_account import TestAdmDeleteAccount
from admin_edit_account import TestAdminEditAccount
from admin_send_notifications import TestAdminNotify
from instructor_access_info import TestInsAccessInfo
from instructor_edit_info import TestInstructEdit
from instructor_view_assignments import TestInstructorViewAssignments

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


runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)