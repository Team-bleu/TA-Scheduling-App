from Command import Command


class CreateCourseCommand(Command):

    def action(self, user_input_list, user, courses, labs):
        pass

    def isCommand(self, command):
        return command == "createcourse"

    def countArgs(self, user_input_list):
        return len(user_input_list) < 2
