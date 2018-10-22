import unittest
import supervisor_assign_TA_lab
import supervisor_show_TA
import admin_send_notifications
import instructor_edit_info
import instructor_assign_TA_lab

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(supervisor_assign_TA_lab.SupAssignTALab))
suite.addTest(unittest.makeSuite(supervisor_show_TA.SupShow))
suite.addTest(unittest.makeSuite(admin_send_notifications.AdminNotify))
suite.addTest(unittest.makeSuite(instructor_edit_info.InstructEdit))
suite.addTest(unittest.makeSuite(instructor_assign_TA_lab.InstructAssignTALab))

runner = unittest.TextTestRunner()
res = runner.run(suite)
print(res)
