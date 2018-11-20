from Command import Command


class LogoutCommand(Command):

    def action(self, user_input_list):

        Command.setLogged(self,False)
        return "logged out."

    def isCommand(self, command):
        return command == "logout"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
