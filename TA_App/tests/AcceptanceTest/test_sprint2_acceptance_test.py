from django.test import TestCase
from application.app import App


class acceptanceTest2(TestCase):
    app = App()

    def test_userstory_12(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add TA1 pass"), "TA1 has been added")
        self.assertEqual(self.app.command("add Instruct1 pass"), "Instruct1 has been added")
        self.assertEqual(self.app.command("role TA1 TA"), "TA1 has become a TA")
        self.assertEqual(self.app.command("role Instruct1 Instructor"), "Instruct1 has become a Instructor")
        self.app.command("remove TA1")
        self.app.command("remove Instruct1")
