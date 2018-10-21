import unittest
from app import App


# 5.
# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester
class SupAssignTALab(unittest.TestCase):
    app = App()

    # First we have the Supervisor, Luke, login
    # with <username>: Luke and <password>: password
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then we have Luke assign the TA, John, the course, CS250
    def test_assign_course(self):
        self.assertEqual(self.app.command("assigncourse John CS250"), "John has been added to the course")

    # Then we assign the TA, John, a lab section from that course, Sec801
    def test_assign_course(self):
        self.assertEqual(self.app.command("assignlab  John Sec801"), "John has been added to Sec801")

    # Then we have the Supervisor logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")
