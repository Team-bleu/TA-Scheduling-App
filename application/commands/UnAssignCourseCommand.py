from Command import Command
from UserUtility import UserUtility
from CourseUtility import CourseUtility


class UnAssignCourseCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"

        userUtil = UserUtility()
        courseUtil = CourseUtility()
        username = str(user_input_list[1]).upper()      # force uppercase
        courseName = str(user_input_list[2]).upper()    # force uppercase

        user = userUtil.searchUser(username)
        if (user == None):
            return username + " does not exist"

        if (courseUtil.getContents(courseName) == False):  # if course doesn't exist, return error
            return "Course doesn't exist"

        if (courseUtil.unAssignCourse(username) == False):
            return username + " is not a part of this course"

        courseUtil.writeContents()

        user.unAssignCourse(courseName)
        userUtil.updateUser(user)

        return "Unassigned "+username+" from "+courseName


    def isCommand(self, command):
        return command == "unassigncourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
