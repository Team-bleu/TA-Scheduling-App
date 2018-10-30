from user import User
from ExampleCommand import ExampleCommand
from LoginCommand import LoginCommand
from LogoutCommand import LogoutCommand


# This class stores all of the commands
# and cycles through them to retrieve
# the correct response when called upon
class CommandsList:
    _current = User()
    _commands = [ExampleCommand, LoginCommand, LogoutCommand]

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

