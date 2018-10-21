import unittest
from app import App


# 9.
# As a Supervisor, I want to access to all
# data in the system, so that I can view or edit data
class SupAssignTALab(unittest.TestCase):
    app = App()

    # First we have the Supervisor, Luke, login
    # with <username>: Luke and <password>: password
    def test_login(self):
        self.assertEqual(self.app.command("login Luke password"), "Luke logged in")

    # Then, we have the Supervisor, Luke, view information
    # from John, the TA. This should print out a dictionary
    # of John's information
    def test_show(self):
        self.assertEqual(self.app.command("show John"), {"name": "John", "phone": "414-123-4567",
                                                         "email": "john@gmail.com",
                                                         "address": "1234 W Number St WI Milwaukee, 53222"})

    # Then we have the Supervisor logout
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "Luke logged out")
