from Command import Command
from UserUtility import UserUtility
from CourseUtility import CourseUtility


class RemoveCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"

        util = UserUtility()
        courseUtil = CourseUtility()
        username = user_input_list[1]

        user = util.searchUser(username)
        if user is None:
            return username + " doesn't exist!"


        if (user.getCourses() is None):
            for i in range(0, user.getCourses().__len__()):
                courseUtil.getContents(user.getCourses()[i])
                courseUtil.unAssignCourse(username)
                courseUtil.writeContents()


        util.removeUser(username)


        return username + " has been removed."

    def isCommand(self, command):
        return command == "remove"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2