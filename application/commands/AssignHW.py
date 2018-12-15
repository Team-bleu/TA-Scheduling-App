
from Command import Command
from CourseUtility import CourseUtility
from UserUtility import UserUtility


class AssignHWCommand(Command):

    def action (self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if not Command.getCredentialss(self) == 2:
            return "Does not have permission"

        # <username> <hw1>
        userUtil = UserUtility()

        username = user_input_list[1]
        homework = user_input_list[2]

        user = userUtil.searchUser(username)

        if (user.getRole() != "TA"):
            return user.getUsername()+" is not a TA"

        # if (user.getLabs() == None or "None"):
        #     return "Can't assign this TA homework because they are not assigned to a lab. "

        user.setAssignment(homework)
        userUtil.updateUser(user)

        return username+" has been assigned "+homework

    def isCommand(self, command):
        return command == "assignHW"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
