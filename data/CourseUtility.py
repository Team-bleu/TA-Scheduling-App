from user import User
from BSTutility import BSTUtility
import os


class CourseUtility:

    _courseName = None
    #_sections = []
    _labs = []
    _instructor = None
    _TAs = None

    def __init__(self):
        self._courseName = None
        #self._sections = [None]
        self._labs = [None]

    def getContents(self, courseName):

        fileName = self.append("courses/",courseName)+".txt"

        if (os.path.isfile(fileName)):      #check if file exists
            file = open(fileName, "r+")
            contents = file.readlines()

            self._courseName = contents[0].replace("\n", "")
            #self._sections = contents[1].replace("\n", "").split(",")
            self._labs = contents[1].replace("\n", "").split(",")
            self._instructor = contents[2].replace("\n", "")
            self._TAs = contents[3].replace("\n", "").split(",")

            file.close()
        else:
            print("Course does not exist\n")

    def writeContents(self, courseName):
        fileName = self.append("courses/", courseName)+".txt"

        file = open(fileName, "w+")

        #write course name to 1st line
        file.write(courseName)

        #write labs to 2nd line
        for x in self._labs:
            file.write(x,",")

        #write instructor to 3rd line
        file.write(self._instructor)

        #write TAs to 4th line
        file.write(self._TAs)

        file.close()

    def getCourseName(self):
        return self._courseName

    def getLabs(self):
        return self._labs

    def getInstructor(self):
        return self._instructor

    def getTAs(self):
        return self._TAs

    def assignLab(self,username, LabName):

        bst = BSTUtility()
        TAobj = bst.searchUser(username)

        if (TAobj.getRole() != "TA"):
            return print(username,"is not a TA")


        count = 0;
        index = -1

        for x in self._labs:

            if (x == LabName):
                index = count
            count = count + 1

        if (index == -1):
            return "Lab doesn't exist"
        else:
            self._TAs[index] = username

    def createCourse(self,courseName):

        fileName = self.append("data/courses/", courseName) + ".txt"

        if (os.path.isfile(fileName)):      #check if file exists already
            print("Course already exists")
        else:
            file = open(fileName, "+w")
            file.write(courseName)
            file.write("\nNone")
            file.write("\nNone")
            file.write("\nNone")
            file.close()
            print(courseName,"has been created")


    def deleteCourse(self,courseName):
        fileName = self.append("data/courses/", courseName) + ".txt"
        os.remove(fileName)


    # This function is used to append two strings together
    # In particular, this function appends a directory with a file
    def append(self, directory, file):
        return directory + file



#print("current directory: ",os.getcwd())

# Testing stuff below

#obj = CourseUtility()
#obj.getContents("CS351")

#obj.assignLab("sffields","Lab802")

#obj.writeContents()

#obj.createCourse("CS351")
#obj.deleteCourse("CS401")

#print("\nCourseName =",obj.getCourseName())

#print("\nSections =",obj.getSections())
#print("\nLabs =",obj.getLabs())
#print("\nInstructor =",obj.getInstructor())
#print("\nTAs =",obj.getTAs())

