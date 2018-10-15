# As a Administrator, I want to send
# notifications to users via email

import unittest
from app import App


def login_prompt():
    user_input = input("Type: login King admin\n")
    return user_input


def notify_prompt():
    user_input = input("Type: notify John Don't forget the grades.")
    return user_input


def logout_prompt():
    user_input = input("Type: logout\n")
    return user_input


class AdminNotification(unittest.TestCase):
    def test_admin_notification(self):
        print("As an Administrator, I want to send\nnotifications to users via email")

        app = App()
        user_input = ""
        user_input_list = [""]
        users = [{"username": "John", "password": "4321", "logged": False, "name": "John", "role": "TA",
                  "course": None, "lab": None, "information": None},
                 {"username": "King", "password": "admin", "logged": False, "name": "King", "role": "Administrator",
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

        # prompts for user to send a notification
        print("\nNow, send a notification")
        while user_input_list[0] != "notify":
            # prompts for user to send notification
            user_input = notify_prompt()
            user_input_list = user_input.split(" ")
            if user_input_list[0] != "notify":
                print("You have to notify a user\n")

        # checks if admin sent a notification
        self.assertEqual(app.command(user_input),
                         "email has been sent")

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
