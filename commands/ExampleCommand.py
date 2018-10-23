from Command import Command


class ExampleCommand(Command):

    def action(self):
        print("This is the example command")
        return

    def isCommand(self, command):
        return command == "example"
