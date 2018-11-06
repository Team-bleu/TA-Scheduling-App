import abc


class Command(abc.ABC):
    logged = False

    def setLogged(self, logged):
        self.logged = logged

    def isLogged(self):
        if self.logged:
            return True
        else:
            return False

    # This performs the action of the command
    @abc.abstractmethod
    def action(self, user_input_list):
        pass

    # This checks if the command matches user's input
    @abc.abstractmethod
    def isCommand(self, command):
        pass

    # This counts the number of arguments given including the command
    @abc.abstractmethod
    def countArgs(self, user_input_list):
        pass

    # This is to test the Example Command, prints statement
    def printExample(self):
        print("This print is from the Command UI")
