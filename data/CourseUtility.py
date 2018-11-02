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

        fileName = self.append("data/courses/",courseName)+".txt"

        #print("fileName =",fileName)

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
            return False

    def writeContents(self):
        fileName = self.append("data/courses/", str(self._courseName))+".txt"

        #print("FileName = ",fileName)
        file = open(fileName, "w+")

        #write course name to 1st line
        file.write(self._courseName+"\n")

        #write labs to 2nd line
        for x in range(0,self._labs.__len__()):
            if (self._labs[x] == None):
                self._labs[x] = "None"
            if (x < self._labs.__len__()-1):
                file.write(self._labs[x]+",")
            else:
                file.write(self._labs[x]+"\n")

        #write instructor to 3rd line
        file.write(str(self._instructor)+"\n")

        #write TAs to 4th line
        for x in range(0,self._TAs.__len__()):
            if (x < self._TAs.__len__()-1):
                if (self._TAs[x] == None): # fill in with "none" if nothing is there
                    file.write("None,")
                else:
                    file.write(self._TAs[x]+",")
            else:
                file.write((self._TAs[x]))

        file.close()

    def getCourseName(self):
        return self._courseName

    def getLabs(self):
        return self._labs

    def getInstructor(self):
        return self._instructor

    def getTAs(self):
        return self._TAs

    def assignCourse(self,username):
        bst = BSTUtility()
        insObj = bst.searchUser(username)
        if (insObj.getRole() != "instructor"):
            return print(username,"is not an instructor")

        self._instructor = insObj.username
        print(username,"has been added to ",self._courseName)
        return


    def assignLab(self,username, LabName):

        bst = BSTUtility()
        TAobj = bst.searchUser(username)

        #print("TA =",TAobj.getUsername())

        if (TAobj.getRole() != "TA"):
            return print(username,"is not a TA")


        count = 0;
        index = -1

        for x in self._labs:
            if (x == LabName):
                index = count
            count = count + 1

        if (index == -1):
            return print(LabName,"doesn't exist")
        else:
            #print("TA size = ",self._TAs.__len__())
            #print("index = ",index)
            if ((index+1) > self._TAs.__len__()):
                TASize = self._TAs.__len__()
                tempTAList = [None]*(index+1)
                for x in range(0,TASize):
                    tempTAList[x] = self._TAs[x]
                self._TAs = tempTAList

            #print("TAs = ",self._TAs)
            #print("tempTAList = ", tempTAList)
            self._TAs[index] = username
            #print("afterTAs = ", self._TAs)


            return print(username,"has been added to",LabName)

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

    def createLab(self, labName):
        index = self._labs.__len__()

        if (self._labs[0] == "None"):   # if there are no labs yet, make this lab the first one
            self._labs[0] = labName
        else:

            #create temp list to store new lab list
            tempLabList = [None] * (index + 1)
            for x in range(0,self._labs.__len__()): # put contents of old list into new list
                if(self._labs[x] == labName):
                    return print("Lab already exists")
                tempLabList[x] = self._labs[x]
            tempLabList[index] = labName

            self._labs = tempLabList

        print(labName,"has been created")



    # This function is used to append two strings together
    # In particular, this function appends a directory with a file
    def append(self, directory, file):
        return directory + file



#print("current directory: ",os.getcwd())

# Testing stuff below

#obj = CourseUtility()
#obj.getContents("CS351")
#print("coursename = ",obj.getCourseName())

#obj.assignLab("sffields","Lab803")
#obj.assignLab("jpbrown","Lab802")

#obj.writeContents()

#obj.createCourse("CS351")
#obj.deleteCourse("CS401")

#print("\nCourseName =",obj.getCourseName())

#print("\nSections =",obj.getSections())
#print("\nLabs =",obj.getLabs())
#print("\nInstructor =",obj.getInstructor())
#print("\nTAs =",obj.getTAs())

