from Command import Command
from CourseUtility import CourseUtility
from UserUtility import UserUtility


class RemoveLabCommand(Command):

    def action(self, user_input_list):

        if not Command.isLogged(self):
            return "No user is logged in."

        if Command.getCredentialss(self) < 2:
            return "Do not have permission"

        # <course> <lab>
        courseUtil = CourseUtility()
        userUtil = UserUtility()

        courseName = user_input_list[1]
        labName = user_input_list[2]

        if (courseUtil.getContents(courseName) == False):
            return courseName + " does not exist"


        # make sure to remove lab from user file
        for i in range(0,courseUtil.getLabs().__len__()):
            if (labName == courseUtil.getLabs()[i]):
                TA = userUtil.searchUser(courseUtil.getTAs()[i])
                if (TA != None):
                    TA.unAssignLab(courseName,labName)
                    userUtil.updateUser(TA)

        if (courseUtil.removeLab(labName) == False):
            return labName + " does not exist"

        courseUtil.writeContents()

        return labName +" has been removed"



    def isCommand(self, command):
        return command == "removelab"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 3