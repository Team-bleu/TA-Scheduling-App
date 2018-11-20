import unittest
from app import App
from UserUtility import UserUtility
from user import User


# 5.
# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester
class TestSignTALab(unittest.TestCase):
    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "Instructor", None, None, None, None, None, None)

    # First we have the Supervisor, Luke, login
    # with <username>: Luke and <password>: password
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

    # Then we have Luke assign the TA, John, the course, CS250
        self.assertEqual(self.app.command("assigncourse John CS351"), "John has been assigned to CS351")

    # Then we assign the TA, John, a lab section from that course, Sec801
        self.assertEqual(self.app.command("assignlab John CS351 Sec801"), "John has been assigned to Sec801")

    # Then we have the Supervisor logout
        self.assertEqual(self.app.command("logout"), "logged out.")
