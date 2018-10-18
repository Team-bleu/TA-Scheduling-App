import unittest
from app import App


# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester
class SupAssignTALab(unittest.TestCase):
    app = App()

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then we assign the TA a course
    def test_assign_course(self):
        self.assertEqual(self.app.command("assigncourse John CS250"), "John has been added to the course")

    # Then we assign the TA a lab
    def test_assign_course(self):
        self.assertEqual(self.app.command("assignlab  John Sec801"), "John has been added to Sec801")

    # Then we have them logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")
