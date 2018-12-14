from Command import Command
from CourseUtility import CourseUtility
from UserUtility import UserUtility


class UnAssignLabCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 2:
            return "Do not have permission"

        # <username> <course> <lab>
        courseUtil = CourseUtility()
        userUtil = UserUtility()

        username = str(user_input_list[1]).upper()      # force uppercase
        courseName = str(user_input_list[2]).upper()    # force uppercase
        labName = str(user_input_list[3]).upper()       # force uppercase

        if (courseUtil.getContents(courseName) == False):
            return courseName + " does not exist"

        user = userUtil.searchUser(username)

        if (user == None):
            return username + " does not exist"
        if (user.unAssignLab(courseName, labName) == False):
            return username + " is not a part of this lab"

        userUtil.updateUser(user)

        courseUtil.unAssignLab(username, labName)
        courseUtil.writeContents()

        return username + " has been unnassigned from " + courseName+"-"+labName



    def isCommand(self, command):
        return command == "unassignlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 4