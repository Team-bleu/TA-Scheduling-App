from user import User
from django.test import TestCase

class UserTest(TestCase):

    def setUp(self):
        self.user0 = User()
        self.user1 = User("Peter", "Xiong", "xiongpp", "admin123", "Instrutor", "phone", "email", "address", "CS351",
                          "lab01", "assignment", "officehours")

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
        self.assertIsNotNone(self.user1.getCourses())
        self.assertEqual(self.user1.getCourses(), "CS351")
        self.assertIsNotNone(self.user1.getLabs())
        self.assertEqual(self.user1.getLabs(), "lab01")

    def test_get_assignment(self):
        self.assertIsNotNone(self.user1.getAssignment())
        self.assertEqual(self.user1.getAssignment(), "assignment")

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


    def test_set_assignment(self):
        self.assertIsNotNone(self.user1.getAssignment())
        self.assertEqual(self.user1.getAssignment(), "assignment")

    def test_get_contents(self):
        self.assertIsNotNone(self.user1.getContents())
        self.assertEqual(self.user1.getContents(), ["Peter", "Xiong", "xiongpp", "admin123", "Instrutor",
                                                    "phone", "email", "address", "CS351",
                                                    "lab01", "assignment", "officehours"])

    def tearDown(self):
        self.emptyUser = None

