import unittest
from app import App
from UserUtility import UserUtility
from user import User


# 17.
# As an Instructor, I want to edit my own information,
# so that others know that I've updated my new phone and address
class TestInstructEdit(unittest.TestCase):
    app = App()
    util = UserUtility()
    user = User("Guy", None, "Guy", "abc123", None, None, None, None, None, None, None)


    # First we have an Instructor, Guy, login
    # with <username>: Guy and <password>: abc123
    def test_login(self):
        # For testing purposes, we'll add a John
        self.util.updateUser(self.user)

        self.assertEqual(self.app.command("login Guy abc123"), "Guy logged in.")

    # Then we have Guy show his current information
    # (should display a dictionary for the info)
        self.assertEqual(self.app.command("show Guy"), {"name": "Guy", "phone": "414-111-2222",
                                                        "email": "guy@gmail.com",
                                                        "address": "4567 W 1st St, Milwaukee WI, 53255"})

    # Then we want the Instructor, Guy, to
    # change that information
        self.assertEqual(self.app.command("edit Guy phone 414-222-1111"), "information updated")

    # The new information should be updated even when viewed
        self.assertEqual(self.app.command("show Guy"), {"name": "Guy", "phone": "414-222-1111",
                                                        "email": "guy@gmail.com",
                                                        "address": "4567 W 1st St, Milwaukee WI, 53255"})

    # Then we have the Instructor logout
        self.assertEqual(self.app.command("logout"), "logged out.")
    util.removeUser("Guy")

