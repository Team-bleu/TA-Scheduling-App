from Command import Command


class QuitCommand(Command):

    def action(self, user_input_list):
        return "Quiting session."

    def isCommand(self, command):
        return command == "quit"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
