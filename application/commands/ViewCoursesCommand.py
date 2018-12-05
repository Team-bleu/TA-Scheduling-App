from Command import Command
from CourseUtility import CourseUtility


class ViewCoursesCommand(Command):

    def action(self, user_input_list):
        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"
        
        courseUtil = CourseUtility()

        courses = courseUtil.viewCourses()

        # if there are no courses, it will print "No courses to show"
        return courses


    def isCommand(self, command):
        return command == "viewcourses"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1
