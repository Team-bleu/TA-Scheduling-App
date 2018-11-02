from Command import Command


class AssignLabCommand(Command):

    def action(self, user_input_list):
        pass

    def isCommand(self, command):
        return command == "assignlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3