from Command import Command


class HelpCommand(Command):

    def action(self, user_input_list):

        role = Command.getCredentialss(self)
        helpString = HelpCommand.getHelp(self,role)

        return helpString

    def isCommand(self, command):
        return command == "help"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 1

    def getHelp(self, role):

        helpString = ""

        addCommandString =      "add <username> <password>\n" \
                                "adds user <username> to the course <coursename>\n\n"

        assignCourseString =    "assigncourse <username> <coursename>\n" \
                                "assigns instructor <username> to course <coursename>\n\n"

        assignLabString =       "assignlab <username> <coursename> <labname>\n" \
                                "assigns TA <username> to lab <labname> of course <coursename>\n\n"

        createCourseString =    "createcourse <coursename>\n" \
                                "creates course <coursename>\n\n"

        createLabString =       "createlab <coursename> <labname>\n" \
                                "creates lab <labname> for course <coursename>\n\n"

        helpCommandString =     "help\n" \
                                "shows a description of all available commands\n\n"

        quitString =            "quit\n" \
                                "logs out the current user\n\n"

        removeString =          "remove <username>\n" \
                                "removes the user <username> from the database\n\n"

        removeCourseString =    "removecourse <coursename>\n" \
                                "removes the course <coursename> from the database\n\n"

        removeLabString =       "removelab <coursename> <labname>\n" \
                                "removes the lab <labname> from course <coursename>\n\n"

        showString =            "show <username>\n " \
                                "shows public information of user <username>\n\n"

        unAssignCourseString =  "unassigncourse <username> <coursename>\n" \
                                "unassigns the instructor <username> from course <coursename>\n\n"

        unAssignLabString =     "unassignlab <username> <coursename> <labname>\n" \
                                "unassigns TA <username> from lab <labname> of course <coursename>\n\n"

        viewCoursesString =      "viewcourses\n" \
                                 "displays all courses in the database\n\n"

        viewAssignmentsString=   "viewassignments <username>\n" \
                                 "view assignments of user <username>\n\n"

        viewUsersString =       "viewusers <role>\n" \
                                "view all users with role <role>, \n" \
                                "by providing 'all' for <role>, all users with be displayed\n\n"



        if (role == 4):     #Supervisor
            helpString = addCommandString + \
                         assignCourseString + \
                         assignLabString + \
                         createCourseString + \
                         createLabString + \
                         helpCommandString + \
                         quitString + \
                         removeString + \
                         removeCourseString + \
                         removeLabString + \
                         showString + \
                         unAssignCourseString + \
                         unAssignLabString + \
                         viewCoursesString + \
                         viewAssignmentsString + \
                         viewUsersString

        elif (role == 3):   #Adminstrator
            helpString = addCommandString + \
                         createCourseString + \
                         createLabString + \
                         helpCommandString + \
                         quitString + \
                         removeString + \
                         removeCourseString + \
                         removeLabString + \
                         showString + \
                         viewCoursesString + \
                         viewAssignmentsString + \
                         viewUsersString

        elif (role == 2):   #Instructor
            helpString = assignLabString + \
                         helpCommandString + \
                         quitString + \
                         showString + \
                         unAssignLabString + \
                         viewCoursesString + \
                         viewAssignmentsString + \
                         viewUsersString

        elif (role == 1):   #TA
            helpString = helpCommandString + \
                         quitString + \
                         showString+ \
                         viewCoursesString + \
                         viewAssignmentsString + \
                         viewUsersString

        return helpString



