import ExampleCommand
import LoginCommand


class CommandsList:
    commands = [ExampleCommand, LoginCommand]

    # This method checks the user input to
    # see if we have a matching command
    def check_command(self, user_input):
        user_input = user_input.split(" ")      # This parses the user's input

        for command in self.commands:
            if command.isCommand(user_input[0]):
                command.action()
