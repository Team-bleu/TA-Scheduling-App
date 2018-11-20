import unittest
from application.app import App


# 22.

# As a TA, I want to view all the TA assignments.

class TestTAViewAssignments(unittest.TestCase):
    app = App()

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        self.assertEqual(self.app.command("viewassignment Paul"), "viewed assignments for Paul")

        # Sally is another TA
        self.assertEqual(self.app.command("viewassignment Sally"), "viewed assignments for Sally")

        # TAs cannot view course assignments
        self.assertEqual(self.app.command("viewassignment CS351"), "Do not have permission")

        # not valid name
        self.assertEqual(self.app.command("viewassignment djofn"), "djofn does not exist")

        self.assertEqual(self.app.command("logout"), "logged out.")
