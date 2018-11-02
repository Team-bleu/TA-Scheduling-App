from user import User
from ExampleCommand import ExampleCommand
from LoginCommand import LoginCommand
from LogoutCommand import LogoutCommand
from AddCommand import AddCommand
from CreateCourseCommand import CreateCourseCommand
from AssignLabCommand import AssignLabCommand
from AssignCourseCommand import AssignCourseCommand
from CreateLabCommand import CreateLabCommand

# This class stores all of the commands
# and cycles through them to retrieve
# the correct response when called upon
class CommandsList:
    _current = User()
    _commands = [ExampleCommand, LoginCommand, LogoutCommand, AddCommand, CreateCourseCommand, AssignLabCommand, AssignCourseCommand, CreateLabCommand]

    # Method for parsing user input into a list
    def parseInput(self, user_input):
        return user_input.split(" ")

    # This method checks the user input to
    # see if we have a matching command
    def checkCommand(self, user_input, user, courses, labs):

        # This parses the user's input
        user_input_list = self.parseInput(user_input)
        cmd = user_input_list[0]

        # Cycles through list of commands to
        # find matching command for action
        for command in self._commands:
            # Does the command match any of the commands in our list?
            if command.isCommand(self, cmd):
                # Does the command have enough arguments to work?
                if command.countArgs(self, user_input_list):
                    return "Not enough arguments."

                # Preforms the command
                return command.action(self, user_input_list, user, courses, labs)

    # Sets the currently logged user
    def setCurrent(self, user):
        self._current = user

    # Checks if there is a user already logged in
    def isCurrent(self):
        return self._current.getUsername() == "None"

    # Simple function to return that there exists no currently logged user
    def logged(self):
        return "No user is logged in. Please login before typing a command."

    # This function returns a rank for the role of the user.
    # The rank is used to determine the role's accessibility,
    # e.g. ranks 3 and 4 can access private info, ranks 1 and 2
    # can access only public info (if rank is 0 then they have no use)
    def getCredentialss(self):
        role = self._current.getRole()
        rank = 0

        if role == "Supervisor":
            rank = 4
        if role == "Administrator":
            rank = 3
        if role == "Instructor":
            rank = 2
        if role == "TA":
            rank = 1

        return rank
