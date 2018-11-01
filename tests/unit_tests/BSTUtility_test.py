import unittest
from BSTutility import BSTUtility
from user import User

# Unittests to test the BST Utility
class BSTUtilityTest(unittest.TestCase):

    def setUp(self):
        self.util = BSTUtility()
        self.user1 = User("first", "last", "user1", "admin123", "role",
                    ["phone", "email", "address"], "course", "lab", "assignment", "None", "None", "None")
        self.user2 = User()
    def test_constructor(self):
        pass

    def test_append(self):
        fileName1 = "CS150.txt"
        fileName2 = "CS351.txt"
        self.assertEqual(self.util.append("data/users/", fileName1), "data/users/CS150.txt")
        self.assertEqual(self.util.append("data/users/", fileName2), "data/users/CS351.txt")
        self.assertEqual(self.util.append("", fileName2), "CS351.txt")
        self.assertEqual(self.util.append("data/users/", ""), "data/users/")

    def test_remove_new_line(self):
        test1 = "Name: Peter\n\n\n Role: TA\n Course: CS250"
        test2 = "this is a test text without any new line character"
        self.assertEqual(self.util.removeNewLine(test1), "Name: Peter Role: TA Course: CS250")
        self.assertEqual(self.util.removeNewLine(test2), "this is a test text without any new line character")

    def test_create_user(self):
        test1 = ["first", "last", "user1", "admin123", "role",
                 "phone", "email", "address", "course", "lab", "assignment", "None", "None", "None"]
        self.assertIsInstance(self.util.createUser(test1), User)
        self.assertEqual(self.util.createUser(test1), self.user1)
        self.assertIsInstance(self.util.createUser(None), User)
        self.assertEqual(self.util.createUser(None), self.user2)

if __name__ == "__main__":
    unittest.main()