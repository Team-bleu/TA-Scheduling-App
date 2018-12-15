from django.test import TestCase
from application.app import App


# test for sprint 3
# https://tree.taiga.io/project/ogarcia27-ta-scheduling-app/taskboard/sprint-2-1328
class acceptanceTest3(TestCase):
    app = App()

    def test_userstory_18(self):
        self.assertEqual(self.app.command("login super pass"), "SUPER logged in.")
        self.assertEqual(self.app.command("viewassignments"), "Does not have permission.")

    def test_userstory_13(self):
        self.assertEqual(self.app.command("login super pass"), "SUPER logged in.")
        self.assertEqual(self.app.command("add instructor password"), "instructor has been added")
        self.assertEqual(self.app.command("viewassignments"), "There are no assignments.")

    def test_userstory_10(self):
        self.assertEqual(self.app.command("login super pass"), "SUPER logged in.")
        self.assertEqual(self.app.command("add instructor password"), "instructor has been added")
        self.assertEqual(self.app.command("add TA1 pass"), "TA1 has been added")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.assertEqual(self.app.command("login instructor password"), "instructor logged in.")
        self.assertEqual(self.app.command("assignHW TA1"), "Not enough arguments")

    def test_userstory_22(self):
        self.assertEqual(self.app.command("login super pass"), "SUPER logged in.")
        self.assertEqual(self.app.command("add instructor password"), "instructor has been added")
        self.assertEqual(self.app.command("add TA1 pass"), "TA1 has been added")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.assertEqual(self.app.command("login instructor password"), "instructor logged in.")
        self.assertEqual(self.app.command("assignHW TA1"), "Not enough arguments")
        self.assertEqual(self.app.command("assignHW TA1 homework1"), "TA1 has been assigned homework1")

    def test_userstory_20(self):
        self.assertEqual(self.app.command("login super pass"), "SUPER logged in.")
        self.assertEqual(self.app.command("add instructor password"), "instructor has been added")
        self.assertEqual(self.app.command("add TA1 pass"), "TA1 has been added")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.assertEqual(self.app.command("login instructor password"), "instructor logged in.")
        self.assertEqual(self.app.command("assignHW TA1"), "Not enough arguments")
        self.assertEqual(self.app.command("assignHW TA1 homework1"), "TA1 has been assigned homework1")
        self.assertEqual(self.app.command("viewassignments"), "User: TA1 Assignment: homework1")

