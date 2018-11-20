from Command import Command
from CourseUtility import CourseUtility
from UserUtility import UserUtility


class AssignLabCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 2:
            return "Do not have permission"

        # <username> <course> <lab>
        courseUtil = CourseUtility()
        userUtil = UserUtility()

        username = user_input_list[1]
        courseName = user_input_list[2]
        labName = user_input_list[3]

        if (courseUtil.getContents(courseName) == False):
            return

        courseUtil.assignLab(username,labName)
        courseUtil.writeContents()

        user = userUtil.searchUser(username)
        user.setClass(courseName,labName)
        userUtil.updateUser(user)

        return username + " has been assigned to " + labName

    def isCommand(self, command):
        return command == "assignlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 4