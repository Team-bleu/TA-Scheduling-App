import unittest
from application.app import App


#2.

#As a supervisor I want to create a new course so that I can assign TA's and instructors.

class TestSupCreateCourse(unittest.TestCase):

    app = App()

    #James is a supervisor
    def test_login(self):
        self.assertEqual(self.app.command("login James password"), "James logged in")
    def test_create_course(self):
        self.assertEqual(self.app.command("createcourse CS351"), "CS351 has been created")
    def test_assign_course(self):
        # John is a TA
        self.assertEqual(self.app.command("assigncourse John CS351"), "John has been added to the course")
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "James logged out")
