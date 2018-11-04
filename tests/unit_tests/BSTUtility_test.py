import unittest
from BSTutility import BSTUtility
from user import User


# Unittests to test the BST Utility
class BSTUtilityTest(unittest.TestCase):

    def setUp(self):
        self.util = BSTUtility()
        self.user1 = User("first", "last", "user1", "admin123", "role",
                          ["phone", "email", "address"], "course", "lab", "assignment", "None", "None", "None")
        self.emptyUser = User()



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


    # I am not sure about this one, if left child is none,
    # shouldn't the method return none instead of an empty user?
    # Also, could you help me add the unit test for testing left child if the current does have left child
    # I am not sure how to set the left child properly
    def test_get_left_child(self):
        self.assertIsInstance(self.util.getLeftChild(), User)
        self.assertEqual(self.util.getLeftChild().getContents(), self.emptyUser.getContents())

    # same issue as the test left child for this one
    def test_get_right_child(self):
        self.assertIsInstance(self.util.getRightChild(), User)
        self.assertEqual(self.util.getRightChild().getContents(), self.emptyUser.getContents())

    #If user does't exist. would it be better to return None than an empty user?
    def test_search_user(self):
        self.assertIsInstance(self.util.searchUser("NotExist"), User)
        self.assertEqual(self.util.searchUser("NotExist").getContents(), self.emptyUser.getContents())
        self.util.addUser(self.user1)
        self.assertIsInstance(self.util.searchUser("user1"), User)
        #this one should not fail, I add user1 and search for user1 but it still failed, not sure why
        self.assertEqual(self.util.searchUser("user1").getContents(), self.user1.getContents())

    # this one is not finsihed
    def test_remove_user(self):
        self.assertIsNone(self.util.removeUser("NotExist"))

    # here is the method I left out. Sorry about that. I understand how the code works
    # but Can't think about a way to properly test them since they don't return anything
    # It would be great if you can help me implement them
    def test_init(self):
        pass
    def test_add_user(self):
        pass
    def test_update_user(self):
        pass
    def test_setup_root(self):
        pass;

    def tearDown(self):

        self.util = None
        self.user1 = self.emptyUser = None



if __name__ == "__main__":
    unittest.main()
