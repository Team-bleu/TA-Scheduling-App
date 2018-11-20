import unittest
from application.app import App

class TestSupCreateAccount(unittest.TestCase):
    app = App()

    def test_remove_Sup(self):
        self.assertEqual(self.app.command("remove John Smith"), "John Smith has been removed")

    def test_assigncourse_Sup(self):
        self.assertEqual(self.app.command("assigncourse John Smith Math100"), "John has been added to Math100")

    def test_add_Admin(self):
        self.assertEqual(self.app.command("add John Smith Username password"), "User John Smith has been created")

    def test_show_Admin(self):
        self.assertEqual(self.app.command("Show John Smith:"), "John Smith’s information: first name, last name, role, phone number, email, address, courses, labs")

    def test_view_Instructor(self):
        self.assertEqual(self.app.command("show Math100"), "TA’s for Math100: ")

    def test_edit_TA(self):
        self.assertEqual(self.app.command("edit John"), "Information updated")