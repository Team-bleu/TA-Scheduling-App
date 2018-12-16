from Command import Command
from UserUtility import UserUtility
from CourseUtility import CourseUtility


class ViewAssignmentsCommand(Command):

    def action (self, user_input_list):
        if not Command.isLogged(self):
            return "No user is logged in."

        if not Command.getCredentialss(self) == 2:
            return "Does not have permission."

        courseUtil = CourseUtility()
        userUtil = UserUtility()

        currentUser = self._logger
        currentUser = userUtil.searchUser(currentUser.getUsername())
        courseList = currentUser.getCourses()
        TAassignments = ""

        for i in range(0, courseList.__len__()):
            TAList = courseUtil.getTAs()
            for x in range(0, TAList.__len__()):
                currentTA = userUtil.searchUser(TAList[x])
                TAassignments += "\n" + "User: " + currentTA + " Assignment:" + currentTA.getAssignment()

        return TAassignments

    def isCommand(self, command):
        return command == "viewassignments"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
