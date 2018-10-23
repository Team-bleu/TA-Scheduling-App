from Command import Command


class ExampleCommand(Command):

    def action(self):
        return "This is the example command"

    def isCommand(self, command):
        return command == "example"
