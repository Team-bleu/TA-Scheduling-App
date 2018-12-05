from Command import Command


class HelpCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        return "Help command string return has to be finished implementing."

    def isCommand(self, command):
        return command == "help"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
