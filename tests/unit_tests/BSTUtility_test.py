import unittest
from BSTutility import BSTUtility
from user import User


# Unittests to test the BST Utility
class BSTUtilityTest(unittest.TestCase):

    def setUp(self):
        self.util = BSTUtility()
        self.user1 = User("first", "last", "user1", "admin123", "role",
                          "phone", "email", "address", "course", "lab", "assignment", "None", "None", "None")
        self.searchuser = User("first", "last", "searchuser", "password", "role",
                          "phone", "email", "address", "course", "lab", "assignment", "None", "None", "None")
        self.emptyUser = User()

        self.util.updateUser(self.searchuser)


    def test_append(self):
        fileName1 = "CS150.txt"
        fileName2 = "CS351.txt"
        self.assertEqual(self.util.append("data/users/", fileName1), "data/users/CS150.txt")
        self.assertEqual(self.util.append("data/users/", fileName2), "data/users/CS351.txt")
        self.assertEqual(self.util.append("", fileName2), "CS351.txt")
        self.assertEqual(self.util.append("data/users/", ""), "data/users/")

    def test_remove_new_line(self):
        test1 = ["Name\n", "LastName\n\n", "Supervisor\n"]
        test2 = ["this is a test text without any new line character"]
        self.assertEqual(self.util.removeNewLine(test1), ["Name", "LastName", "Supervisor"])
        self.assertEqual(self.util.removeNewLine(test2), ["this is a test text without any new line character"])

    def test_create_user(self):
        test1 = ["first", "last", "user1", "admin123", "role",
                 "phone", "email", "address", "course", "lab", "assignment", "None", "None", "None"]
        self.assertIsInstance(self.util.createUser(test1), User)
        self.assertEqual(self.util.createUser(test1).getContents(), self.user1.getContents())

    def test_get_left_child(self):
        self.assertIsInstance(self.util.getLeftChild(), User)
        self.assertEqual(self.util.getLeftChild().getContents(), self.emptyUser.getContents())

    def test_get_right_child(self):
        self.assertIsInstance(self.util.getRightChild(), User)
        self.assertEqual(self.util.getRightChild().getContents(), self.emptyUser.getContents())

    #If user does't exist. would it be better to return None than an empty user?
    def test_search_user(self):
        self.assertEqual(self.util.searchUser("NotExist"), None)

        # We must reset the utility before looking for the new user
        self.util.setUp()
        self.assertIsInstance(self.util.searchUser("searchuser"), User)
        self.assertEqual(self.util.searchUser("searchuser").getContents(), self.searchuser.getContents())
        # Now we must reset the utility and remove the dummy user
        # But the line below doesn't work. Manually delete searchuser.txt
        # and update the neighbors.
        self.assertIsNone(self.util.removeUser("searchuser"))

    # this one is not finsihed
    def test_remove_user(self):
        self.assertIsNone(self.util.removeUser("NotExist"))

    # I'm not sure if we can test an initialization of the utility object
    # without adding getters for the dataset
    def test_init(self):
        pass

    def test_update_user(self):
        self.util.updateUser(self.searchuser)
        # If the user "searchuser" has been added correctly, we can verify its contents
        self.assertEqual(self.util.searchUser("searchuser").getContents(), self.searchuser.getContents())
        self.assertIsNone(self.util.removeUser("searchuser"))

    def test_add_user(self):
        self.util.addUser(self.searchuser)
        # If the user "searchuser" has been added correctly, we can verify its contents
        # same reason as update user test
        self.assertEqual(self.util.searchUser("searchuser").getContents(), self.searchuser.getContents())
        self.assertIsNone(self.util.removeUser("searchuser"))

    def test_setup_root(self):
        self.assertIsInstance(self.util.setUpRoot(), User)
        # Here, our root will be super.txt
        self.assertEqual(self.util.setUpRoot().getUsername() + ".txt", "super.txt")

    def tearDown(self):
        self.util = None
        self.user1 = self.emptyUser = None



if __name__ == "__main__":
    unittest.main()
