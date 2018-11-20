from application.CommandsList import CommandsList


class App:
    commands = CommandsList()

    users = []
    courses = []
    labs = []

    # user_input is what the user typed on the command line
    # the return value will be the application's response
    def command(self, user_input):
        return self.commands.checkCommand(user_input)

    def done(self):
        return True  # will let user know that they're done
