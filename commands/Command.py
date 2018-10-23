import abc


class Command(abc.ABC):

    # This performs the action of the command
    @classmethod
    def action(self):
        pass

    # This checks if the command matches user's input
    @classmethod
    def isCommand(self, command):
        pass
