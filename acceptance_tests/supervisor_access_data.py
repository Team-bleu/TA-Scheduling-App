# As a Supervisor, I want to access all
# of the data in the system

import unittest
from app import App

auto_input = True


def login_prompt():
    if auto_input:
        user_input = "login Luke password"
    else:
        user_input = input("Type: login Luke password\n")
    return user_input


def show_prompt():
    if auto_input:
        user_input = "show John"
    else:
        user_input = input("Type: show John\n")
    return user_input


def logout_prompt():
    if auto_input:
        user_input = "logout"
    else:
        user_input = input("Type: logout\n")
    return user_input


class SupervisorCheckInfo(unittest.TestCase):
    def test_supervisor_check_info(self):
        print("\nAs a Supervisor, I want to access\nall of the data in the system")

        app = App()
        user_input = ""
        user_input_list = [""]
        users = [{"username": "John", "password": "4321", "logged": False, "name": "John", "role": "TA",
                  "course": None, "lab": None,
                  "information": {"name": "John", "phone": "414-123-4567", "email": "john@gmail.com",
                                  "address": "1234 W Number St WI Milwaukee, 53222"}},
                 {"username": "Luke", "password": "password", "logged": False, "name": "Luke", "role": "Supervisor",
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
                         users[1].get("username") + " logged in")

        # prompts for use to get information of another user
        print("\nLook up information.")
        while user_input_list[0] != "show":
            # prompts for showing information of a user
            user_input = show_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "show":
                print("You have to make a request to show user information")

        # checks if user correctly viewed another user's information
        self.assertEqual(app.command(user_input),
                         users[0].get("information"))

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
