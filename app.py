from CommandsList import CommandsList


class App:
    commands = CommandsList()

    users = []
    courses = []
    labs = []

    # user_input is what the user typed on the command line
    # the return value will be the application's response
    def command(self, user_input):
        response = self.commands.check_command(user_input, self.users, self.courses, self.labs)

        # This checks if response is a string, if not then, print nothing
        # (otherwise, it'll print None every time an incorrect command is used
        if response:
            print(response)

    def done(self):
        return True  # will let user know that they're done
