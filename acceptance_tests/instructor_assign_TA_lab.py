import unittest
from app import App


# 21.
# As an Instructor, I want to assign my TA a lab section,
# so that they know what lab they'll teach for the semester
class SupAssignTALab(unittest.TestCase):
    app = App()

    # with <username>: Guy and <password>: abc123
    def test_login(self):
        self.assertEqual(self.app.command("login Guy abc123"), "Guy logged in")

    # Then we assign the TA, John, a lab section from that course, Sec802
    def test_assign_course(self):
        self.assertEqual(self.app.command("assignlab John Sec802"), "John has been added to Sec802")

    # Then we have the Instructor logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Guy logged out")
