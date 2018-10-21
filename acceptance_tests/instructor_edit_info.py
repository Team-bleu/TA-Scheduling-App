import unittest
from app import App


# 17.
# As an Instructor, I want to edit my own information,
# so that others know that I've updated my new phone and address
class InstructEdit(unittest.TestCase):
    app = App()

    # First we have an Instructor, Guy, login
    # with <username>: Guy and <password>: abc123
    def test_login(self):
        self.assertEqual(self.app.command("login Guy abc123"), "Guy logged in")

    # Then we have Guy show his current information
    # (should display a dictionary for the info)
    def test_assign_course(self):
        self.assertEqual(self.app.command("show Guy"), {"name": "Guy", "phone": "414-111-2222",
                                                         "email": "guy@gmail.com",
                                                         "address": "4567 W 1st St, Milwaukee WI, 53255"})

    # Then we want the Instructor, Guy, to
    # change that information
    def test_assign_course(self):
        self.assertEqual(self.app.command("edit Guy phone 414-222-1111"), "information updated")

    # The new information should be updated even when viewed
    def test_assign_course(self):
        self.assertEqual(self.app.command("show Guy"), {"name": "Guy", "phone": "414-222-1111",
                                                         "email": "guy@gmail.com",
                                                         "address": "4567 W 1st St, Milwaukee WI, 53255"})

    # Then we have the Instructor logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Guy logged out")
