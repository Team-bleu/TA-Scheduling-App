import abc
from app import App


class AcceptanceUI(abc):
    users = [{"username": "John", "password": "4321", "logged": False, "name": "John Will", "role": "TA",
             "course": "CS250", "lab": ["Sec801", "Sec802"],
              "information": {"phone": "414-123-4567", "email": "john@gmail.com",
                              "address": "1234 W Number St WI Milwaukee, 53222"}},
             {"username": "Indigo", "password": "abcd", "logged": False, "name": "Indigo Red", "role": "Instructor",
              "course": "CS250", "lab": None,
              "information": {"phone": "414-765-4321", "email": "indigo@gmail.com",
                              "address": "5678 E 1st St WI Milwaukee, 53200"}},
             {"username": "King", "password": "admin", "logged": False, "name": "King Guy", "role": "Administrator",
              "course": None, "lab": None,
              "information": {"phone": "414-111-2222", "email": "king@gmail.com",
                              "address": "1000 W Sky St WI Milwaukee, 53222"}},
             {"username": "Luke", "password": "password", "logged": False, "name": "Luke Dude", "role": "Supervisor",
              "course": None, "lab": None,
              "information": {"phone": "414-000-0000", "email": "luke@gmail.com",
                              "address": "0000 W Super Ave WI Milwaukee, 53222"}}]
    app = App()

