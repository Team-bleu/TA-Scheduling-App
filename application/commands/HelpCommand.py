from Command import Command


class HelpCommand(Command):

    def action(self, user_input_list):

        file = open("./application/files/designDoc.txt", "r+")
        contents = file.read()

        return contents

    def isCommand(self, command):
        return command == "help"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
