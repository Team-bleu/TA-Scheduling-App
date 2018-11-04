import unittest
from user import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.user0 = User()
        self.user1 = User("Peter", "Xiong", "xiongpp", "admin123", "Instrutor", "phone", "email", "address", "CS351",
                          "lab01", "assignment","super",None,None)

    def test_init(self):
        self.assertIsNotNone(User())
        self.assertIsInstance(User(), User)

    def test_get_name(self):
        self.assertIsNotNone(self.user1.getFirstName())
        self.assertEqual(self.user1.getFirstName(), "Peter")
        self.assertIsNotNone(self.user1.getLastName())
        self.assertEqual(self.user1.getLastName(), "Xiong")

    def test_get_account(self):
        self.assertIsNotNone(self.user1.getUsername())
        self.assertEqual(self.user1.getUsername(), "xiongpp")
        self.assertIsNotNone(self.user1.getPassword())
        self.assertEqual(self.user1.getPassword(), "admin123")

    def test_get_role(self):
        self.assertIsNotNone(self.user1.getRole())
        self.assertEqual(self.user1.getRole(), "Instrutor")

    def test_get_info(self):
        self.assertIsNotNone(self.user1.getInfo())
        self.assertEqual(self.user1.getInfo(), ["phone", "email", "address"])

    def test_get_class_info(self):
        self.assertIsNotNone(self.user1.getCourse())
        self.assertEqual(self.user1.getCourse(), "CS351")
        self.assertIsNotNone(self.user1.getLab())
        self.assertEqual(self.user1.getLab(), "lab01")

    def test_get_assignment(self):
        self.assertIsNotNone(self.user1.getAssignment())
        self.assertEqual(self.user1.getAssignment(), "assignment")

    def test_get_parent_left_right_node(self):
        self.assertIsNotNone(self.user1.getParent())
        self.assertEqual(self.user1.getParent(), "super")
        self.assertIsNone(self.user1.getLeftChild())
        self.assertIsNone(self.user1.getRightChild())

    def test_set_name(self):
        self.user0.setName("Peter", "Xiong")
        self.assertIsNotNone(self.user0.getFirstName())
        self.assertEqual(self.user0.getFirstName(), "Peter")
        self.assertIsNotNone(self.user0.getLastName())
        self.assertEqual(self.user0.getLastName(), "Xiong")

    def test_set_account(self):
        self.user0.setAccount("xiongpp", "admin123")
        self.assertIsNotNone(self.user0.getUsername())
        self.assertEqual(self.user0.getUsername(), "xiongpp")
        self.assertIsNotNone(self.user0.getPassword())
        self.assertEqual(self.user0.getPassword(), "admin123")

    def test_set_role(self):
        self.user0.setRole("Instrutor")
        self.assertIsNotNone(self.user0.getRole())
        self.assertEqual(self.user0.getRole(), "Instrutor")

    def test_set_info(self):
        self.user0.setInfo("phone", "email", "address")
        self.assertIsNotNone(self.user0.getInfo())
        self.assertEqual(self.user0.getInfo(), ["phone", "email", "address"])

    def test_set_class_info(self):
        self.user0.setClass("CS351","lab01")
        self.assertIsNotNone(self.user0.getCourse())
        self.assertEqual(self.user0.getCourse(), "CS351")
        self.assertIsNotNone(self.user0.getLab())
        self.assertEqual(self.user0.getLab(), "lab01")

    def test_set_assignment(self):
        self.assertIsNotNone(self.user1.getAssignment())
        self.assertEqual(self.user1.getAssignment(), "assignment")

    def test_set_parent_left_right_node(self):
        self.user0.setParent("super")
        self.assertIsNotNone(self.user0.getParent())
        self.assertEqual(self.user0.getParent(), "super")
        self.user1.setLeftChild("left1")
        self.user1.setRightChild("right1")
        self.assertIsNotNone(self.user1.getLeftChild())
        self.assertEqual(self.user1.getLeftChild(), "left1")
        self.assertIsNotNone(self.user1.getRightChild())
        self.assertEqual(self.user1.getRightChild(), "right1")

    def test_get_contents(self):
        self.assertIsNotNone(self.user1.getContents())
        self.assertEqual(self.user1.getContents(), ["Peter", "Xiong", "xiongpp", "admin123", "Instrutor",
                                                    "phone", "email", "address", "CS351",
                                                    "lab01", "assignment","super",None,None])

    def tearDown(self):
        self.emptyUser = None

