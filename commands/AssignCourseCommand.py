from Command import Command
from BSTutility import BSTUtility
from CourseUtility import CourseUtility
from Command import Command


class AssignCourseCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."
        
        bstUtil = BSTUtility()
        courseUtil = CourseUtility()
        username = user_input_list[1]
        courseName = user_input_list[2]

        if (courseUtil.getContents(courseName) == False):   #if course doesn't exist, return error
            return

        courseUtil.assignCourse(username)
        courseUtil.writeContents()

        user = bstUtil.searchUser(username)
        user.setClass(courseName,"None")
        bstUtil.updateUser(user)

    def isCommand(self, command):
        return command == "assigncourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
