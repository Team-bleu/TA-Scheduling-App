import unittest
from acceptance_test_UI import AcceptanceUI


# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester
class SupAssignTALab(AcceptanceUI, unittest.TestCase):

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login " + self.users[3]["username"] + " " + self.users[3]["password"]),
                         self.users[3]["username"] + " logged in")

    # Then we assign the TA a course
    def test_assign_course(self):
        self.assertEqual(self.app.command("assigncourse " + self.users[0]["name"] + " " + self.courses[0]["course"]),
                         self.users[0]["name"] + " has been added to the course")

    # Then we assign the TA a lab
    def test_assign_course(self):
        self.assertEqual(self.app.command("assignlab  " + self.users[0]["name"] + " " + self.courses[0]["labs"][0]),
                         self.users[0]["name"] + " has been added to " + self.courses[0]["labs"][0])

    # Then we have them logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), self.users[3]["username"] + " logged out")
