from django.test import TestCase
from application.app import App
from CourseUtility import CourseUtility


class acceptanceTest(TestCase):
    app = App()

    def setUp(self):
        self.courseUtil = CourseUtility()

    # 7(Sprint 1) a Supervisor, I want to have a user interface so that I can login and logout my account
    def test_login(self):
        self.assertEqual(self.app.command("login super"), "Not enough arguments.")
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("login super 123"), "Wrong password.")
        self.assertEqual(self.app.command("login user pass"), "No such user exists.")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 7(Sprint 1) a Supervisor, I want to have a user interface so that I can login and logout my account
    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 3(Sprint 1) As a Supervisor, I want to create accounts
    def test_create_user(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add user1"), "Not enough arguments.")
        self.assertEqual(self.app.command("add user1 admin123"), "user1 has been added")
        self.assertEqual(self.app.command("add user1 admin123"), "User already exists.")
        self.assertEqual(self.app.command("add user1"), "Not enough arguments.")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 2(Sprint 1) As a supervisor I want to create a new course so that I can assign TA's and instructors.
    def test_supervisor_create_course(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS361"), "CS361 has been created")
        self.assertEqual(self.app.command("createcourse"), "Not enough arguments.")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.courseName = "CS361"
        self.courseUtil.getContents(self.courseName)
        self.courseUtil.deleteCourse()

    # 2(Sprint 1) As a supervisor I want to create a new course so that I can assign TA's and instructors.
    def test_non_supervisor_create_course(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("createcourse CS361"), "Do not have permission")
        self.assertEqual(self.app.command("createcourse CS251"), "Do not have permission")
        self.assertEqual(self.app.command("logout"), "logged out.")


    # 8(Sprint 1) As a supervisor I want to assign TAs to courses so that the TAs can be assigned to a lab section
    def test_supervisor_assign_course(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS351"), "CS351 has been created")
        self.assertEqual(self.app.command("assigncourse TA1 CS351"), "TA1 is not an Instructor")
        self.assertEqual(self.app.command("assigncourse TA1"), "Not enough arguments.")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.courseName = "CS351"
        self.courseUtil.getContents(self.courseName)
        self.courseUtil.deleteCourse()


    # 8(Sprint 1) As a supervisor I want to assign TAs to courses so that the TAs can be assigned to a lab section
    def test_non_supervisor_assign_course(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("createcourse CS351"), "Do not have permission")
        self.assertEqual(self.app.command("assigncourse TA1 CS351"), "Do not have permission")
        self.assertEqual(self.app.command("logout"), "logged out.")


    # 5(Sprint 1) As a supervisor I want to assign TAs to particular lab sections so that they know what lab to teach.
    def test_supervisor_create_lab(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS361"), "CS361 has been created")
        self.assertEqual(self.app.command("createlab CS361 lab801"), "lab801 has been created")
        self.assertEqual(self.app.command("createlab CS361 lab802"), "lab802 has been created")
        self.assertEqual(self.app.command("createlab CS361"), "Not enough arguments.")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.courseName = "CS361"
        self.courseUtil.getContents(self.courseName)
        self.courseUtil.deleteCourse()

    # 5(Sprint 1) As a supervisor I want to assign TAs to particular lab sections so that they know what lab to teach.
    def test_non_supervisor_create_lab(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("createlab CS361 lab801"), "Do not have permission")
        self.assertEqual(self.app.command("createlab CS251 lab801"), "Do not have permission")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 5(Sprint 1) As a supervisor I want to assign TAs to particular lab sections so that they know what lab to teach.
    def test_supervisor_assign_lab(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS351"), "CS351 already exists")
        self.assertEqual(self.app.command("createlab CS351 lab801"), "lab801 has been created")
        self.assertEqual(self.app.command("createlab CS351 lab802"), "lab802 has been created")
        self.assertEqual(self.app.command("assignlab TA1 CS351 lab801"), "TA1 is already assigned to CS351-lab801")
        self.assertEqual(self.app.command("assignlab CS361"), "Not enough arguments.")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.courseName = "CS351"
        self.courseUtil.getContents(self.courseName)
        self.courseUtil.deleteCourse()

    def test_non_supervisor_assign_lab(self):
        self.assertEqual(self.app.command("login user1 admin123"), "user1 logged in.")
        self.assertEqual(self.app.command("assignlab TA1 CS351 LAB801"), "Do not have permission")
        self.assertEqual(self.app.command("logout"), "logged out.")

    def test_logout(self):
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 11(Sprint 2) As an administrator I want to be able to delete accounts
    def test_admin_delete(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add user2"), "Not enough arguments.")
        self.assertEqual(self.app.command("add user2 admin123"), "user2 has been added")
        self.assertEqual(self.app.command("add user2 admin123"), "User already exists.")
        self.assertEqual(self.app.command("remove user2"), "user2 has been removed.")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 14 (Sprint 2) As an administrator I want to be able to edit accounts
    def test_admin_edit_info(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add user2 admin123"), "user2 has been added")
        self.assertEqual(self.app.command("edit user2 "), "information updated")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 16 (Sprint 2) As an administrator I want to access all the data in the system
    def test_admin_show(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add user2 admin123"), "User already exists.")
        self.assertEqual(self.app.command("show user2"), "First Name: first\nLast Name: last\nemail: email\nphone: phone\naddress: address")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 19 (Sprint 2) As an instructor I want to read public contact information
    def test_instructor_show(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add user2 admin123"), "User already exists.")
        self.assertEqual(self.app.command("show user2"), "First Name: first\nLast Name: last\nemail: email\nphone: phone\naddress: address")
        self.assertEqual(self.app.command("logout"), "logged out.")

    # 24 (Sprint 2) As a TA I want to edit my own information so that the administrator and supervisor have access to it
    def test_TA_edit_info(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("edit phone, email, address, first name, last name"), "phone, doesn't exist!")
        self.assertEqual(self.app.command("logout"), "logged out.")

