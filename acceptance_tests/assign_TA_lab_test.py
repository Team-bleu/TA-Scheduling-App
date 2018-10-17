# As a Supervisor, I want to assign a TA a lab section,
# so that they know what lab they'll teach for the semester

import unittest
from app import App

auto_input = True


def login_prompt():
    if auto_input:
        user_input = "login Luke password"
    else:
        user_input = input("Type: login Luke password\n")
    return user_input


def assign_prompt():
    if auto_input:
        user_input = "assignlab John Sec801"
    else:
        user_input = input("Type: assignlab John\n")
    return user_input


def logout_prompt():
    if auto_input:
        user_input = "logout"
    else:
        user_input = input("Type: logout\n")
    return user_input


class AssignTALab(unittest.TestCase):
    def test_assign_ta_lab_test(self):
        print("\nUser story: As a Supervisor, I want to assign a TA a lab section,"
              "\nso that they know what lab they'll teach for the semester.\n")

        app = App()
        user_input = ""
        user_input_list = [""]
        users = [{"username": "John", "password": "4321", "logged": False, "name": "John", "role": "TA",
                 "course": None, "lab": None, "information": None},
                 {"username": "Luke", "password": "password", "logged": False, "name": "Luke", "role": "Supervisor",
                 "course": None, "lab": None, "information": None}]
        courses = [{"course": "CS150", "labs": ["Sec801", "Sec802", "Sec803"]}]

        # creates a new user
        for each_user in users:
            user_input = "add" + each_user["username"] + " " + each_user["password"]
            app.command(user_input)

        # adds a course
        app.command("createcourse CS150")

        for each_course in courses:
            for each_lab in each_course["labs"]:
                user_input = "createlab" + each_course["course"] + " " + each_lab
                app.command(user_input)

        # prompts for user to login
        print("\nLogin the user.")
        while user_input_list[0] != "login":
            # prompts for user to login
            user_input = login_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "login":
                print("You have to login\n")

        # checks if user has logged in
        self.assertEqual(app.command(user_input),
                         users[1].get("username") + " logged in")

        # prompts for assign lab command
        print("\nNow, assign the TA a lab course.")
        while user_input_list[0] != "assignlab":
            # prompts for new user
            user_input = assign_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "assignlab":
                print("You have to assign a lab to the TA")

        # checks if TA has been added to the lab
        self.assertEqual(app.command(user_input),
                         users[0].get("name") + " has been added to " + user_input_list[2])

        # prompts for logout command
        print("\nNow, logout the user.\n")
        while user_input_list[0] != "logout":
            # prompts for logout
            user_input = logout_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "logout":
                print("You have to logout")

        # checks if user has been logged out
        self.assertEqual(app.command(user_input),
                         users[1].get("username") + " logged out")
