from CommandsList import CommandsList


class App:
    commands = CommandsList()

    users = []
    courses = []
    labs = []

    # userString is what the user typed on the command line
    # the return value will be the applications response
    def command(self, user_input):
        return self.commands.check_command(user_input)

    def done(self):
        return True  # will let user know that they're done
