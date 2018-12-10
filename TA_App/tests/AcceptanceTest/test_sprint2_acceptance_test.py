from django.test import TestCase
from application.app import App


# test for sprint 2
# https://tree.taiga.io/project/ogarcia27-ta-scheduling-app/taskboard/sprint-2-1328
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

    def test_userstory_11(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add account password"), "account has been added")
        self.assertEqual(self.app.command("remove account"), "account has been removed.")

    def test_userstory_4(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add account password"), "account has been added")
        self.assertEqual(self.app.command("remove account"), "account has been removed.")

    def test_userstory_9(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("add dude asdf"), "dude has been added")
        self.assertEqual(self.app.command("show dude"), "First Name: first\nLast Name: last\nemail: email\nphone: "
                                                        "phone\naddress: address\nOffice Hours: officehours")
        self.app.command("remove dude")

    def test_userstory_19(self):
        self.app.command("login super pass")
        self.app.command("add instruct pass")
        self.app.command("add ta pass")
        self.app.command("role instruct Instructor")
        self.app.command("role ta TA")
        self.assertEqual(self.app.command("login instruct pass"), "instruct logged in.")
        self.assertEqual(self.app.command("show ta"), "First Name: first\nLast Name: last\nemail: email\n"
                                                      "Office Hours: officehours")
        self.assertEqual(self.app.command("logout"), "logged out.")
        self.app.command("login super pass")
        self.app.command("remove instruct")
        self.app.command("remove ta")

    def test_userstory_16(self):
        self.app.command("login super pass")
        self.app.command("add admin pass")
        self.app.command("role admin Administrator")
        self.assertEqual(self.app.command("login admin pass"), "admin logged in.")
        self.assertEqual(self.app.command("add dude asdf"), "dude has been added")
        self.assertEqual(self.app.command("show dude"), "First Name: first\nLast Name: last\nemail: email\nphone: "
                                                        "phone\naddress: address\nOffice Hours: officehours")
        self.app.command("remove dude")
        self.app.command("remove admin")

    def test_userstory_17(self):
        self.app.command("login super pass")
        self.app.command("add instruct pass")
        self.app.command("role instruct Instructor")
        self.assertEqual(self.app.command("login instruct pass"), "instruct logged in.")
        self.assertEqual(self.app.command("edit instruct firstname Doug lastname Idea "
                                          "phone 414-123-4567 email doug@uwm.edu"),
                         "information updated")
        self.app.command("login super pass")
        self.app.command("remove instruct")

    def test_userstory_24(self):
        self.app.command("login super pass")
        self.app.command("add ta pass")
        self.app.command("role ta TA")
        self.assertEqual(self.app.command("login ta pass"), "ta logged in.")
        self.assertEqual(self.app.command("edit ta firstname Donny lastname Idea "
                                          "phone 414-123-4567 email doug@uwm.edu"),
                         "information updated")
        self.app.command("login super pass")
        self.app.command("remove ta")

    def test_userstory_6(self):
        self.app.command("login super pass")
        self.app.command("add ta pass")
        self.app.command("role ta TA")
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("edit ta firstname Donny lastname Idea "
                                          "phone 414-123-4567 email doug@uwm.edu"),
                         "information updated")
        self.app.command("login super pass")
        self.app.command("remove ta")

    def test_userstroy_14(self):
        self.app.command("login super pass")
        self.app.command("add ta pass")
        self.app.command("role ta TA")
        self.app.command("add admin pass")
        self.app.command("role admin Administrator")
        self.assertEqual(self.app.command("login admin pass"), "admin logged in.")
        self.assertEqual(self.app.command("edit ta firstname Donny lastname Idea "
                                          "phone 414-123-4567 email doug@uwm.edu"),
                         "information updated")
        self.app.command("login super pass")
        self.app.command("remove ta")
        self.app.command("remove admin")

    def test_userstory_15(self):
        self.assertEqual(self.app.command("login super pass"), "super logged in.")
        self.assertEqual(self.app.command("createcourse CS100"), "CS100 has been created")
        self.app.command("removecourse CS100")

    def test_userstory_21(self):
        self.app.command("login super pass")
        self.app.command("add instruct pass")
        self.app.command("role instruct Instructor")
        self.app.command("add ta pass")
        self.app.command("role ta TA")
        self.app.command("createcourse CS250")
        self.app.command("assigncourse instruct CS250")
        self.app.command("createlab CS250 LAB801")
        self.assertEqual(self.app.command("login instruct pass"), "instruct logged in.")
        self.assertEqual(self.app.command("assignlab ta CS250 LAB801"), "ta has been assigned to LAB801")
        self.app.command("removecourse CS250")
        self.app.command("remove ta")
        self.app.command("remove instruct")
