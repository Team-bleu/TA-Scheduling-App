from UserUtility import UserUtility
import os
from TA_Scheduling_App.models import Account, Class, Instructor, TA, Lab, Relationship


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

        fileName = self.append("application/data/courses/",courseName)+".txt"

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
            #print("Course does not exist\n")
            return False

    def writeContents(self):
        fileName = self.append("application/data/courses/", str(self._courseName))+".txt"

        #print("FileName = ",fileName)
        file = open(fileName, "w+")

        #write course name to 1st line
        file.write(self._courseName+"\n")


        # Database Code for updating coursename:    # probably do not need this
        #if (Class.objects.filter(course= self._courseName)):    #if this course already exists in database, set dbCourseName to it
        #    dbCourseName = Class.objects.filter(course= self._courseName)
        #else:
        #    dbCourseName = Class(course=self._courseName)       # else create new element in database
        #    dbCourseName.save()
        # dbCourseName = Class(course=self._courseName)
        # dbCourseName.save()


        #write labs to 2nd line
        for x in range(0,self._labs.__len__()):
            if (self._labs[x] == None):
                self._labs[x] = "None"
            if (x < self._labs.__len__()-1):
                file.write(self._labs[x]+",")
            else:
                file.write(self._labs[x]+"\n")

        # Database Code updating labs:
        labListString = self.listToString(self._labs)

        if (Lab.objects.filter(lab= labListString)):
            dbLabs = Lab.objects.get(lab=labListString)
            #dbLabs = Lab.objects.filter(lab= labListString)
        else:
            dbLabs = Lab(lab= labListString)
            dbLabs.save()
        #dbLabs = Class(labs=labListString)
        #dbLabs.save()

        #write instructor to 3rd line
        file.write(str(self._instructor)+"\n")

        # Database Code updating instructor:
        instructorName = str(self._instructor)
        if (Instructor.objects.filter(instructor= instructorName)):
            #dbInstructor = Instructor.objects.filter(instructor= instructorName)
            dbInstructor = Instructor.objects.get(instructor= instructorName)
        else:
            dbInstructor = Instructor(instructor= instructorName)
            dbInstructor.save()
        #dbInstructor = Class(instructor=self._instructor)
        #dbInstructor.save()

        #write TAs to 4th line
        for x in range(0,self._TAs.__len__()):
            if (x < self._TAs.__len__()-1):
                if (self._TAs[x] == None): # fill in with "none" if nothing is there
                    file.write("None,")
                else:
                    file.write(self._TAs[x]+",")
            else:
                file.write((self._TAs[x]))

        # Database Code updating TAs:
        TAListString = self.listToString(self._TAs)
        if (TA.objects.filter(ta= TAListString)):
            dbTAs = TA.objects.get(ta=TAListString)
            #dbTAs = TA.objects.filter(ta= TAListString)
        else:
            dbTAs = TA(ta= TAListString)
            dbTAs.save()
        #dbTAs = Class(ta=TAListString)
        #dbTAs.save()

        # Database Code to update this Course

        #Lab.objects.all().delete()
        #Instructor.objects.all().delete()
        #TA.objects.all().delete()
        #return

        if (Class.objects.filter(course= self._courseName)):
            dbCourse = Class.objects.get(course=self._courseName)
            #dbCourse = Class.objects.filter(course= self._courseName)
            dbCourse.labs = dbLabs
            dbCourse.instructor = dbInstructor
            dbCourse.ta = dbTAs
            dbCourse.save()
            #dbCourse.update(labs=dbLabs, instructor=dbInstructor, ta=dbTAs)
        else:
            dbCourse = Class(course= self._courseName, labs= dbLabs, instructor= dbInstructor, ta= dbTAs)
            dbCourse.save()
        #dbCourse = Class.objects.filter(course=self._courseName)
        #dbCourse.update(course= dbCourseName, labs= dbLabs, instructor= dbInstructor, ta= dbTAs)
        # if course didn't exist yet, should maybe use dbCourse.save()


        file.close()

    def getCourseName(self):
        return self._courseName

    def getLabs(self):
        return self._labs

    def getInstructor(self):
        return self._instructor

    def getTAs(self):
        return self._TAs

    #assign this course to this instructor, return old instructor if there is one, else return "None"
    def assignCourse(self,username):
        util = UserUtility()
        #insObj = util.searchUser(username)
        oldInstructor = "None"

        if (self._instructor != "None"):
            oldInstructor = self._instructor

        self._instructor = username

        # Database Code:
        #dbInstructor = Instructor(instructor=username)
        #dbInstructor.save()

        user = Account.objects.get(username=username)
        course = Class.objects.get(course=self._courseName)
        lab = Lab.objects.get(lab="None")
        relationship = Relationship.objects.filter(course=course)
        if relationship:
            relationship = Relationship.objects.filter(course=course)
            relationship.update(user=user)
        else:
            relationship = Relationship(user=user, course=course, labs=lab)
            relationship.save()

        return oldInstructor


        #if (insObj.getRole() != "Instructor"): #and insObj.getRole() != "TA"):
        #    return False

        #if (insObj.getRole() == "Instructor"):
        #    self._instructor = insObj.username
        # print(username, "has been added to", self._courseName)

        #return True

    #unassign instructors or TAs from this class, could also use this for unassignlab
    def unAssignCourse(self,username):
        util = UserUtility()
        user = util.searchUser(username)

        if (user.getRole() == "TA"):    # if the user is a TA, search through the TAs and remove them for this course
            changed = False
            for i in range(0, self._TAs.__len__()):
                if (username == self._TAs[i]):
                    self._TAs[i] = "None"
                    changed = True
                    #return True #removed TA
            return changed

        if (user.getRole() == "Instructor"):  # if the user is a TA, search through the TAs and remove them for this course

            if (username == self._instructor):
                self._instructor = "None"
                return True # removed instructor
            else:
                return False    # this user was not the instructor, so nothing changes

        #return False    # return False if no user was unassigned

    def assignLab(self,username, LabName):

        courseLabName = self._courseName+"-"+LabName
        #print("courselabname = ",courseLabName)

        util = UserUtility()
        TAobj = util.searchUser(username)

        #print("TA =",TAobj.getUsername())

        if (TAobj.getRole() != "TA"):   # this shouldn't occur
            return "None" #print(username,"is not a TA")

        count = 0;
        index = -1

        for x in self._labs:
            if (x == LabName):
                index = count
            count = count + 1

        if (index == -1):   # this shouldn't occur
            return "None"  # " lab doesn't exist"

        else:
            if ((index+1) > self._TAs.__len__()):
                TASize = self._TAs.__len__()
                tempTAList = ["None"]*(index+1)
                for x in range(0,TASize):
                    tempTAList[x] = self._TAs[x]
                self._TAs = tempTAList

            oldTA = self._TAs[index]
            self._TAs[index] = username
            return oldTA

    # unassign a TA from a lab, return True if successful, else False
    def unAssignLab(self, userName, labName):

        for i in range(0,self._labs.__len__()):
            if (labName == self._labs[i]):
                if (userName == self._TAs[i]):
                    self._TAs[i] = "None"
                    return True
        return False



    def createCourse(self, courseName):

        fileName = self.append("application/data/courses/", courseName) + ".txt"


        #dbInstructor = Instructor.objects.filter(instructor="None")
        #if (Instructor.objects.filter(instructor="None")):
        #    print("It exists")
        #else:
        #    print("it does not exist")

        #dbInstructor = Instructor.objects.get(instructor="None")
        #Lab.objects.all().delete()
        #Instructor.objects.all().delete()
        #TA.objects.all().delete()
        #newInstructor = Instructor(instructor= "None")
        #newInstructor.save()
        #dbInstructor = Instructor.objects.get(instructor="None")
        #return

        if os.path.isfile(fileName):      # Check if file exists already
            return False  #"Course already exists"
        else:
            file = open(fileName, "+w")
            file.write(courseName)
            file.write("\nNone")
            file.write("\nNone")
            file.write("\nNone")
            file.close()


            # Database code below:

            if (Lab.objects.filter(lab= "None")):
                lab = Lab.objects.get(lab="None")
            else:
                lab = Lab(lab="None")
                lab.save()
            #lab = Lab(lab="None")

            if (Instructor.objects.filter(instructor="None")):
                instructor = Instructor.objects.get(instructor="None")
            else:
                instructor = Instructor(instructor="None")
                instructor.save()
            #instructor = Instructor(instructor="None")

            if (TA.objects.filter(ta="None")):
                ta = TA.objects.get(ta="None")
            else:
                ta = TA(ta="None")
                ta.save()
            #ta = TA(ta="None")


            if (Class.objects.filter(course=courseName)):
                course = Class.objects.filter(course=courseName)
                course.update(labs=lab, instructor=instructor, ta=ta)
            else:
                course = Class(course=courseName, labs=lab, instructor=instructor, ta=ta)
                course.save()

            return True #courseName + " has been created"

    def deleteCourse(self):
        fileName = self.append("application/data/courses/", self._courseName) + ".txt"

        userUtil = UserUtility()

        # if there is an instructor assigned to this course, remove this course from them
        if (self._instructor != "None"):
            user = userUtil.searchUser(self._instructor)
            user.unAssignCourse(self._courseName)
            #user.setClass("None", "None")
            userUtil.updateUser(user)

        # if there are TAs assigned to this course, remove this course from them
        if (self._TAs != "None"):
            for i in range(0,self._TAs.__len__()):
                user = userUtil.searchUser(self._TAs[i])
                if (user != None):
                    user.unAssignCourse(self._courseName)
                    #user.setClass("None","None")
                    userUtil.updateUser(user)


        #Database Code:
        course = Class.objects.filter(course=self._courseName)
        course.delete()



        os.remove(fileName)

    def removeLab(self,labName):

        userUtil = UserUtility()

        if (self._labs == None):
            return "There are no Labs to remove"

        for i in range(0,self._labs.__len__()):
            if (self._labs[i] == labName):
                self._labs[i] = "None"                           # set this lab to None
                if (self._TAs[i] != None):                      # check if there is a TA for that Lab
                    user = userUtil.searchUser(self._TAs[i])    # if there is a TA assigned, search for that TA
                    self._TAs[i] = "None"                       # set the TA for this lab to None
                    if (user != None):                          # if the TA user exists, remove that lab from them
                        #user.setClass(self._courseName,"None")
                        userUtil.updateUser(user)
                self.cleanUpLabList()
                return True

        return False

    #remove any "None"s from the list
    def cleanUpList(self, origList):

        tempListOld = list(origList)
        newSize = tempListOld.__len__()

        for i in range(0,tempListOld.__len__()):
            if (tempListOld[i] == "None"):
                newSize = newSize - 1

        if (newSize != tempListOld.__len__()):
            tempListNew = [None]*(newSize)
            for i in range(0,tempListOld):
                if (tempListOld[i] != "None"):
                    tempListNew[i] = tempListOld[i]

            origList = tempListNew # set original list to this new list without "None"s

        return origList

    def cleanUpLabList(self):

        tempOldLabList = self._labs
        tempOldTAList = self._TAs
        newSize = self._labs.__len__()
        index = 0

        for i in range(0,tempOldLabList.__len__()):
            if (tempOldLabList[i] == "None"):
                newSize = newSize - 1

        if (newSize == 0):  # if all elements in list are gone, make sure to leave one "None"
            tempListNew = ["None"] * (1)
            self._labs = tempListNew    # set both labs and TAs list to one "None"
            self._TAs = tempListNew
            return

        if (newSize != tempOldLabList.__len__()):
            tempNewLabList = [None] * (newSize)
            tempNewTAList  = [None] * (newSize)
            for i in range(0, tempOldLabList.__len__()):
                if (tempOldLabList[i] != "None"):
                    tempNewLabList[index] = tempOldLabList[i]
                    tempNewTAList[index] = tempOldTAList[i]
                    index = index + 1
            self._labs = tempNewLabList
            self._TAs  = tempNewTAList



    # return False if lab already exists, if not, create the lab and return true
    def createLab(self, labName):
        index = self._labs.__len__()

        if (self._labs[0] == "None"):   # if there are no labs yet, make this lab the first one
            self._labs[0] = labName
        else:

            #create temp list to store new lab list
            tempLabList = [None] * (index + 1)
            for x in range(0,self._labs.__len__()): # put contents of old list into new list
                if(self._labs[x] == labName):
                    return False
                tempLabList[x] = self._labs[x]
            tempLabList[index] = labName

            self._labs = tempLabList

        return True


    #used to access _labs or _TAs as a string
    def listToString(self, dataList):

        #to be safe
        if (dataList == None):
            return "None"

        newList = list(dataList)

        listString = ""

        for i in range(0, newList.__len__()):
            if (newList[i] == None):
                listString = "None"
            if (i < newList.__len__() - 1):
                listString = listString + str(newList[i]) + ","
            else:
                listString = listString + str(newList[i])

        return listString





    # This function is used to append two strings together
    # In particular, this function appends a directory with a file
    def append(self, directory, file):
        return directory + file



#print("current directory: ",os.getcwd())

# Testing stuff below

#obj = CourseUtility()
#obj.getContents("CS251")
#string = obj.listToString(obj.getLabs())
#print("string = ",string)
#obj.writeContents()

