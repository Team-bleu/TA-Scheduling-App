import abc


class Command(abc.ABC):

    # This performs the action of the command
    @classmethod
    def action(cls, user_input_list, user, courses, labs):
        pass

    # This checks if the command matches user's input
    @classmethod
    def isCommand(cls, command):
        pass

    # This is to test the Example Command, prints statement
    def printExample(self):
        print("This print is from the Command UI")
