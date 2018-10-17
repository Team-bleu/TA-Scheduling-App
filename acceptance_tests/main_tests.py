import unittest
import supervisor_access_data
import assign_TA_lab_test
import admin_send_notification
import instructor_assign_TA_lab
import instructor_edit_own_info


def main_tests():
    suite = unittest.TestSuite()

    # Add in the tests to the suite
    suite.addTest(unittest.makeSuite(supervisor_access_data.SupervisorCheckInfo))
    suite.addTest(unittest.makeSuite(assign_TA_lab_test.AssignTALab))
    suite.addTest(unittest.makeSuite(admin_send_notification.AdminNotification))
    suite.addTest(unittest.makeSuite(instructor_edit_own_info.InstructorEdit))
    suite.addTest(unittest.makeSuite(instructor_assign_TA_lab.AssignTALab))

    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)
