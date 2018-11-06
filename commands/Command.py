import abc


class Command(abc.ABC):
    logged = False
    _logger = None #User()

    def setLogged(self, logged):
        self.logged = logged

    def isLogged(self):
        if self.logged:
            return True
        else:
            return False

    def setLogger(self,logger):
        self._logger = logger

    # This function returns a rank for the role of the user.
    # The rank is used to determine the role's accessibility,
    # e.g. ranks 3 and 4 can access private info, ranks 1 and 2
    # can access only public info (if rank is 0 then they have no use)
    def getCredentialss(self):
        if self._logger is None:
            return 0
        role = self._logger.getRole()
        rank = 0

        if role == "Supervisor":
            rank = 4
        if role == "Administrator":
            rank = 3
        if role == "Instructor":
            rank = 2
        if role == "TA":
            rank = 1

        return rank

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
