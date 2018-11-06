import unittest
from app import App



class acceptanceTest(unittest.TestCase):
    app = App()

    # 7(Sprint 1) a Supervisor, I want to have a user interface so that I can login and logout my account
    def test_login(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("login super 123"), "Wrong password.")
        self.assertEqual(self.app.command("login user pass"), "No such user exists.")

    # 7(Sprint 1) a Supervisor, I want to have a user interface so that I can login and logout my account
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 3(Sprint 1) As a Supervisor, I want to create accounts
    def test_create_user(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add user1 admin123"), "user1 has been added")
        self.assertEqual(self.app.command("add user1 admin123"), "User already exists.")

    # 2(Sprint 1) As a supervisor I want to create a new course so that I can assign TA's and instructors.
    def test_supervisor_create_course(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS361"), "CS361 has been created")

    # 2(Sprint 1) As a supervisor I want to create a new course so that I can assign TA's and instructors.
    def test_non_supervisor_create_course(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("createcourse CS361"), "Do not have permission")
        self.assertEqual(self.app.command("createcourse CS251"), "Do not have permission")

    # 8(Sprint 1) As a supervisor I want to assign TAs to courses so that later, the TAs can be assigned to a lab section
    def test_supervisor_assign_course(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS351"), "CS351 has been created")
        self.assertEqual(self.app.command("assigncourse TA1 CS351"), "TA1 has been assigned to CS351")

    # 8(Sprint 1) As a supervisor I want to assign TAs to courses so that later, the TAs can be assigned to a lab section
    def test_non_supervisor_assign_course(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("createcourse CS351"), "Do not have permission")
        self.assertEqual(self.app.command("assigncourse TA1 CS351"), "Do not have permission")

    # 5(Sprint 1) As a supervisor I want to assign TAs to particular lab sections so that they know what lab to teach.
    def test_supervisor_create_lab(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createlab CS361 lab801"), "lab801 has been created")
        self.assertEqual(self.app.command("createlab CS361 lab802"), "lab802 has been created")

    # 5(Sprint 1) As a supervisor I want to assign TAs to particular lab sections so that they know what lab to teach.
    def test_non_supervisor_create_lab(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("createlab CS361 lab801"), "Do not have permission")
        self.assertEqual(self.app.command("createlab CS251 lab801"), "Do not have permission")

    # 5(Sprint 1) As a supervisor I want to assign TAs to particular lab sections so that they know what lab to teach.
    def test_supervisor_assign_lab(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createlab CS351 lab801"), "lab801 has been created")
        self.assertEqual(self.app.command("createlab CS351 lab802"), "lab802 has been created")
        self.assertEqual(self.app.command("assignlab TA1 CS351 LAB801"), "TA1 has been assigned to LAB801")




