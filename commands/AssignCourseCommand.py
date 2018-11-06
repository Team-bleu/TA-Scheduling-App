from Command import Command
from CommandsList import CommandsList


class AssignCourseCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        if not CommandsList.getCredentialss() >= 4:
            return "Error. Current User does not have permission to assign course."
        
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
