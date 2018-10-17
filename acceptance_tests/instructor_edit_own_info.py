# As an Instructor, I want to edit my own information
# so that others can see my updated information

import unittest
from app import App

auto_input = True


def login_prompt():
    if auto_input:
        user_input = "login Indigo abcd"
    else:
        user_input = input("Type: login Indigo abcd\n")
    return user_input


def edit_prompt():
    if auto_input:
        user_input = "edit Indigo"
    else:
        user_input = input("Type: edit Indigo\n")
    return user_input


def logout_prompt():
    if auto_input:
        user_input = "logout"
    else:
        user_input = input("Type: logout\n")
    return user_input


class InstructorEdit(unittest.TestCase):
    def test_instructor_edit(self):
        print("As an Instructor, I want to edit my own information\n"
              "so that others can see my updated information")

        app = App()
        user_input = ""
        user_input_list = [""]
        users = [{"username": "Indigo", "password": "abcd", "logged": False, "name": "Indigo", "role": "Instructor",
                  "course": None, "lab": None, "information": None}]

        # creates a new user
        for each_user in users:
            user_input = "add" + each_user["username"] + " " + each_user["password"]
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
                         users[0].get("username") + " logged in")

        # prompts for user to edit information
        print("\nEdit your information.")
        while user_input_list[0] != "edit":
            # prompts for user to edit information
            user_input = edit_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "edit":
                print("You have to edit information\n")

        # checks if user has edited their information correctly
        self.assertEqual(app.command(user_input),
                         "information updated")

        # prompts for logout command
        print("\nNow, logout the user.")
        while user_input_list[0] != "logout":
            # prompts for logout
            user_input = logout_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "logout":
                print("You have to logout")

        # checks if user has been logged out
        self.assertEqual(app.command(user_input),
                         users[1].get("username") + " logged out")
