import unittest
from application.app import App


#22.

#As a TA, I want to view all the TA assignments.

class TestTAViewAssignments(unittest.TestCase):
    app = App()
    # Paul is a TA
    def test_login(self):
        self.assertEqual(self.app.command("login Paul password"), "Paul logged in")
    def test_view(self):
        self.assertEqual(self.app.command("viewassignment Paul"), "viewed assignments for Paul")
        # Sally is another TA
        self.assertEqual(self.app.command("viewassignment Sally"), "viewed assignments for Sally")
        # TAs cannot view course assignments
        self.assertEqual(self.app.command("viewassignment CS351"), "Do not have permission")
        # not valid name
        self.assertEqual(self.app.command("viewassignment djofn"), "djofn does not exist")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Paul logged out")