from Command import Command
from UserUtility import UserUtility
from CourseUtility import CourseUtility


class AssignCourseCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 3:
            return "Do not have permission"
        
        userUtil = UserUtility()
        courseUtil = CourseUtility()
        username = str(user_input_list[1]).upper()      # force uppercase
        courseName = str(user_input_list[2]).upper()    # force uppercase

        if (courseUtil.getContents(courseName) == False):   #if course doesn't exist, return error
            return "Course doesn't exist"

        user = userUtil.searchUser(username)
        if (user == None):
            return username + " does not exist"

        if (user.getRole() != "Instructor"):
            return username + " is not an Instructor"

        # if there was an instructor assigned to this course, make sure to unassign them
        oldInstructor = courseUtil.assignCourse(username)

        if (oldInstructor != "None"):

            if (oldInstructor == username):
                return username + " is already assigned to " + courseName

            oldUser = userUtil.searchUser(oldInstructor)
            if (oldUser != None):
                oldUser.unAssignCourse(courseName)
                userUtil.updateUser(oldUser)


        courseUtil.writeContents()


        if (user.assignCourse(courseName) == False):
            return username + " is already assigned to " + courseName

        userUtil.updateUser(user)

        return username + " has been assigned to " + courseName

    def isCommand(self, command):
        return command == "assigncourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3
