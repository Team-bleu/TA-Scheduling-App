import unittest
from app import App
from UserUtility import UserUtility
from user import User


# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester
class TestSupAssignTALab(unittest.TestCase):
    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "Instructor", None, None, None, None, None, None)

    # First we have the Supervisor login
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

    # Then we assign the TA a course
        self.assertEqual(self.app.command("assigncourse John CS351"), "John has been assigned to CS351")

    # Then we assign the TA a lab
        self.assertEqual(self.app.command("assignlab John CS351 Sec801"), "John has been assigned to Sec801")

    # Then we have them logout
        self.assertEqual(self.app.command("logout"), "logged out.")

#3,7,11,15, 19, 23