import unittest
from UserUtility import UserUtility
from user import User

class UserUtilityTest(unittest.TestCase):

    def test_searchUser(self):
        util = UserUtility()
        user = util.searchUser("dude")
