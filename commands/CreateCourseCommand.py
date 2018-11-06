from Command import Command
from CommandsList import CommandsList


class CreateCourseCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        if not CommandsList.getCredentialss() >= 3:
            return "Error. Current User does not have permission to create courses."
        
        courseUtil = CourseUtility()
        courseName = user_input_list[1]


        courseUtil.createCourse(courseName)


    def isCommand(self, command):
        return command == "createcourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
