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
            return courseName + " does not exist"

        labFound = False
        for i in range(0, courseUtil.getLabs().__len__()):
            if (labName == courseUtil.getLabs()[i]):
                labFound = True
                break
        if (labFound == False):
            return labName + " does not exist"

        user = userUtil.searchUser(username)
        if (user == None):
            return username + " does not exist"

        if (user.getRole() != "TA"):
            return user.getUsername()+" is not a TA"

        oldTA = courseUtil.assignLab(username,labName)

        if (oldTA != "None"):
            if (oldTA == username):
                return username + " is already assigned to " + courseName+"-"+labName
            oldUser = userUtil.searchUser(oldTA)
            if (oldUser != None):
                oldUser.unAssignLab(courseName,labName)
                userUtil.updateUser(oldUser)


        courseUtil.writeContents()

        #user = userUtil.searchUser(username)
        #user.setClass(courseName,courseName+"-"+labName)

        # we know the course and lab already exist, so assign them to this user
        if (user.assignLab(courseName,labName) == False):
            return username + " is already assigned to " + courseName+"-"+labName

        userUtil.updateUser(user)

        return username + " has been assigned to " + labName

    def isCommand(self, command):
        return command == "assignlab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 4