import unittest
from application.app import App


# 21.
# As an Instructor, I want to assign my TA a lab section,
# so that they know what lab they'll teach for the semester
class InstructAssignTALab(unittest.TestCase):
    app = App()

    # with <username>: Guy and <password>: abc123
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

    # Then we assign the TA, John, a lab section from that course, Sec802
        self.assertEqual(self.app.command("assignlab John CS351 Sec802"), "John" " has been assigned to" " Sec802")
        # Not enough arguments

    # Then we have the Instructor logout
        self.assertEqual(self.app.command("logout"), "logged out.")
