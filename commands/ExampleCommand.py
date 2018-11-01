from Command import Command


# This is an example of what a command
# should look like. They should inherit
# from the Command interface and implement
# action() to perform the command's action
# and isCommand() to check if the command
# matches.
class ExampleCommand(Command):

    def action(self, user_input_list):
        print("This is the example command")
        Command.printExample(self)
        return "This is the output string"

    def isCommand(self, command):
        return command == "example"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
