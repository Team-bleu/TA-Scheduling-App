import abc


class Command(abc.ABC):

    # This performs the action of the command
    @classmethod
    def action(cls, user_input_list):
        pass

    # This checks if the command matches user's input
    @classmethod
    def isCommand(cls, command):
        pass
