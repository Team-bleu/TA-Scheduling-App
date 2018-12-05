from LoginCommand import LoginCommand
from LogoutCommand import LogoutCommand
from AddCommand import AddCommand
from CreateCourseCommand import CreateCourseCommand
from AssignLabCommand import AssignLabCommand
from AssignCourseCommand import AssignCourseCommand
from CreateLabCommand import CreateLabCommand
from RoleCommand import RoleCommand
from RemoveCommand import RemoveCommand
from QuitCommand import QuitCommand
from EditCommand import EditCommand
from ShowCommand import ShowCommand
from RemoveLabCommand import RemoveLabCommand
from RemoveCourseCommand import RemoveCourseCommand
from UnAssignCourseCommand import UnAssignCourseCommand
from UnAssignLabCommand import UnAssignLabCommand
from HelpCommand import HelpCommand

# This class stores all of the commands
# and cycles through them to retrieve
# the correct response when called upon
class CommandsList:
    logged = False
    _logger = None
    _commands = [LoginCommand, LogoutCommand, AddCommand, CreateCourseCommand, AssignLabCommand,
                 AssignCourseCommand, CreateLabCommand, RoleCommand, RemoveCommand, QuitCommand,
                 ShowCommand, EditCommand, RemoveLabCommand, RemoveCourseCommand, UnAssignCourseCommand,
                 UnAssignLabCommand, HelpCommand]

    # Method for parsing user input into a list
    def parseInput(self, user_input):
        return user_input.split(" ")

    # This method checks the user input to
    # see if we have a matching command
    def checkCommand(self, user_input):

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
                return command.action(self, user_input_list)
