from ExampleCommand import ExampleCommand
from LoginCommand import LoginCommand


class CommandsList:
    commands = [ExampleCommand, LoginCommand]

    # Method for parsing user input into a list
    def parse_user_input(self, user_input):
        return user_input.split(" ")

    # This method checks the user input to
    # see if we have a matching command
    def check_command(self, user_input):

        # This parses the user's input
        user_input_list = self.parse_user_input(user_input)
        cmd = user_input_list[0]

        # Cycles through list of commands to
        # find matching command for action
        for command in self.commands:
            if command.isCommand(self, cmd):
                command.action(self, user_input_list)
