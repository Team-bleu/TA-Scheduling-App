from Command import Command
from CourseUtility import CourseUtility
from BSTutility import BSTUtility
from Command import Command


class AssignLabCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 2:
            return "Do not have permission"

        # <username> <course> <lab>
        courseUtil = CourseUtility()
        bstUtil = BSTUtility()

        username = user_input_list[1]
        courseName = user_input_list[2]
        labName = user_input_list[3]

        if (courseUtil.getContents(courseName) == False):
            return

        courseUtil.assignLab(username,labName)
        courseUtil.writeContents()

        user = bstUtil.searchUser(username)
        user.setClass(courseName,labName)
        bstUtil.updateUser(user)

        return username + " has been assigned to " + labName

    def isCommand(self, command):
        return command == "assignlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 4