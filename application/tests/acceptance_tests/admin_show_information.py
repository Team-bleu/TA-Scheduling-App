import unittest
from app import App
from UserUtility import UserUtility
from user import User


# 16

# As an Administrator, I want to access all the data in the system

class TestAdminInfo(unittest.TestCase):

    app = App()
    util = UserUtility()
    user = User("John", None, "John", None, None, None, None, None, None, None, None)

    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")

        # For testing purposes we'll add a John
        self.util.updateUser(self.user)
        self.assertEqual(self.app.command("show John"), "First Name: John" +
                                                        "\nLast Name: None" +
                                                        "\nemail: None" +
                                                        "\nphone: None" +
                                                        "\naddress: None")

        # not valid name
        
        self.assertEqual(self.app.command("show djofn"), "djofn doesn't exist!")
        
        self.assertEqual(self.app.command("logout"), "logged out.")
