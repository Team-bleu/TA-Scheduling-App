import unittest
from app import App
from UserUtility import UserUtility
from user import User


# 9.
# As a Supervisor, I want to access to all
# data in the system, so that I can view or edit data
class TestSupShow(unittest.TestCase):
    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, "TA", None, None, None, None, None, None)

    # First we have the Supervisor, super, login
    # with <username>: super and <password>: pass
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

    # Then, we have the Supervisor, super, view information
    # from John, the TA. This should print out a dictionary
    # of John's information
        self.assertEqual(self.app.command("show John"), {"name": "John", "phone": "414-123-4567",
                                                         "email": "john@gmail.com",
                                                         "address": "1234 W Number St WI Milwaukee, 53222"})

    # Then we have the Supervisor logout
        self.assertEqual(self.app.command("logout"), "logged out.")
        util = UserUtility()
        util.removeUser("John")
