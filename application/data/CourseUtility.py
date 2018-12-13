from UserUtility import UserUtility
import os
from TA_Scheduling_App.models import Class, Instructor, TA, Lab, Account, Relationship


class CourseUtility:

    _courseName = None
    _labs = []
    _instructor = None
    _TAs = None

    def __init__(self):
        self._courseName = None
        self._labs = [None]

    #   getContents() opens the file "courseName".txt if it exists, reads all contents
    #       and puts the data into CourseUtility variables accordingly
    #       returns True if file exists
    #       returns False if file does not exist
    def getContents(self, courseName):

        fileName = self.append("application/data/courses/",courseName)+".txt"

        if (os.path.isfile(fileName)):      #check if file exists
            file = open(fileName, "r+")
            contents = file.readlines()

            self._courseName = contents[0].replace("\n", "")
            self._labs = contents[1].replace("\n", "").split(",")
            self._instructor = contents[2].replace("\n", "")
            self._TAs = contents[3].replace("\n", "").split(",")

            file.close()
            return True
        else:
            # Course does not exist
            return False

    #   writeContents() writes all the contents of this course to its .txt file
    #       This is used for updating a course's .txt file (Ex: CS251.txt) with
    #       the updated data which is stored in the CourseUtility Variables
    def writeContents(self):
        fileName = self.append("application/data/courses/", str(self._courseName))+".txt"

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

        # Convert Lab list to a single string
        labListString = self.listToString(self._labs)

        #write instructor to 3rd line
        file.write(str(self._instructor)+"\n")

        # Database Code for updating instructor:
        instructorName = str(self._instructor)
        if (Instructor.objects.filter(instructor= instructorName)):
            #dbInstructor = Instructor.objects.filter(instructor= instructorName)
            dbInstructor = Instructor.objects.get(instructor= instructorName)
        else:
            dbInstructor = Instructor(instructor= instructorName)
            dbInstructor.save()

        #write TAs to 4th line
        for x in range(0,self._TAs.__len__()):
            if (x < self._TAs.__len__()-1):
                if (self._TAs[x] == None): # fill in with "none" if nothing is there
                    file.write("None,")
                else:
                    file.write(self._TAs[x]+",")
            else:
                file.write((self._TAs[x]))

        # Convert TA list to a single string
        TAListString = self.listToString(self._TAs)

        # Database Code to update this Course
        if (Class.objects.filter(course= self._courseName)):
            dbCourse = Class.objects.get(course=self._courseName)
            dbCourse.labs = labListString
            dbCourse.instructor = dbInstructor
            dbCourse.ta = TAListString
            dbCourse.save()
        else:
            dbCourse = Class(course=self._courseName, labs=labListString, instructor=dbInstructor, ta=TAListString)      #new
            dbCourse.save()

        file.close()

    def getCourseName(self):
        return self._courseName

    def getLabs(self):
        return self._labs

    def getInstructor(self):
        return self._instructor

    def getTAs(self):
        return self._TAs

    #   assignCourse() assigns this course to this instructor
    #       returns old instructor if there is one
    #       returns "None" otherwise
    def assignCourse(self,username):
        util = UserUtility()
        oldInstructor = "None"

        if (self._instructor != "None"):
            oldInstructor = self._instructor

        self._instructor = username

        #TODO noticed this code crashes if a saved user starts with uppercase letter, but is searched by starting with lowercase letter
        #TODO this was discovered by using assigncourse command (Ex: savedUser= "Instruct", but user types "assigncourse instruct CS251")

        #Database Relationship Code:
        user = Account.objects.get(username=username)
        course = Class.objects.get(course=self._courseName)
        if not Lab.objects.filter(lab="None"):
            lab = Lab(lab="None")
            lab.save()
        else:
            lab = Lab.objects.get(lab="None")
        relationship = Relationship.objects.filter(course=course)
        if relationship:
            relationship = Relationship.objects.filter(course=course)
            relationship.update(user=user)
        else:
            relationship = Relationship(user=user, course=course, labs=lab)
            relationship.save()
        #End of Relationship Code

        return oldInstructor


    #   unAssignCourse() unassigns instructors or TAs from this class
    #       returns True if there is a change
    #       returns False if there is no change
    def unAssignCourse(self,username):
        util = UserUtility()
        user = util.searchUser(username)

        if (user.getRole() == "TA" and self._TAs is not None):    # if the user is a TA, search through the TAs and remove them for this course
            changed = False
            for i in range(0, self._TAs.__len__()):
                if (username == self._TAs[i]):
                    self._TAs[i] = "None"
                    changed = True
            return changed

        if (user.getRole() == "Instructor"):  # if the user is a TA, search through the TAs and remove them for this course

            if (username == self._instructor):

                self._instructor = "None"

                return True     # removed instructor
            else:
                return False    # this user was not the instructor, so nothing changes


    #   only used with Remove and Role Commands, this removes database instructor file from database
    def removeDBInstructor(self,username):
        if (Instructor.objects.filter(instructor= username)):
            dbInstruct = Instructor.objects.get(instructor= username)
            dbInstruct.delete()
        return


    #   assignLab() assigns the TA "username" to the this lab "LabName"
    #       returns the previous TA of this lab if there was one
    #       returns "None" otherwise
    def assignLab(self,username, LabName):

        courseLabName = self._courseName+"-"+LabName

        util = UserUtility()
        TAobj = util.searchUser(username)

        if (TAobj.getRole() != "TA"):   # this shouldn't occur
            return "None"   # username is not a TA

        count = 0;
        index = -1

        for x in self._labs:
            if (x == LabName):
                index = count
            count = count + 1

        if (index == -1):   # this shouldn't occur
            return "None"   # lab doesn't exist
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

        return "None"

    #   unAssignLab() unassigns the TA "userName" from the lab "labName
    #       returns True if successful
    #       returns False otherwise
    def unAssignLab(self, userName, labName):

        for i in range(0,self._labs.__len__()):
            if (labName == self._labs[i]):
                if (userName == self._TAs[i]):
                    self._TAs[i] = "None"
                    return True
        return False

    #   createCourse() creates a .txt file for this course (Ex: CS251.txt) if this course didn't exist yet
    #       This also adds the newly created course to "courses.txt" (the file that keeps a list of all courses)
    #       returns True if the course .txt file is successfully created
    #       returns False if course already exists
    def createCourse(self, courseName):

        fileName = self.append("application/data/courses/", courseName) + ".txt"

        if os.path.isfile(fileName):      # Check if file exists already
            return False  # Course already exists
        else:
            file = open(fileName, "+w")
            file.write(courseName)
            file.write("\nNone")
            file.write("\nNone")
            file.write("\nNone")
            file.close()

            self.addToMasterCourseList(courseName)  #add course to courses.txt


            # Database code for Instructor below:
            if (Instructor.objects.filter(instructor= "None")):
                instructor = Instructor.objects.get(instructor= "None")
            else:
                instructor = Instructor(instructor= "None")
                instructor.save()

            # create the database file for this course
            if (Class.objects.filter(course=courseName)):
                course = Class.objects.get(course= courseName)
                course.update(labs="None", instructor=instructor, ta="None")
            else:
                course = Class(course=courseName, labs="None", instructor=instructor, ta="None")
                course.save()

            return True     # course has been created

    #   deleteCourse() deletes the .txt file and database file of this course
    #       this also removes this course from courses.txt (the file that keeps a list of all courses)
    def deleteCourse(self):
        fileName = self.append("application/data/courses/", self._courseName) + ".txt"
        userUtil = UserUtility()

        # if there is an instructor assigned to this course, remove this course from them
        if (self._instructor != "None"):
            user = userUtil.searchUser(self._instructor)
            user.unAssignCourse(self._courseName)
            userUtil.updateUser(user)

        # if there are TAs assigned to this course, remove this course from them
        if (self._TAs != "None"):
            for i in range(0,self._TAs.__len__()):
                user = userUtil.searchUser(self._TAs[i])
                if (user != None):
                    user.unAssignCourse(self._courseName)
                    userUtil.updateUser(user)

        #Database Code:
        course = Class.objects.filter(course=self._courseName)
        course.delete()

        os.remove(fileName)
        self.removeFromMasterCourseList(self._courseName)  # remove this course from courses.txt

    #   removeLab() removes the lab "labName" for this course if it exists
    #       returns True if lab is removed
    #       returns False if lab doesn't exist
    def removeLab(self,labName):

        userUtil = UserUtility()

        if (self._labs == None):    # this shouldn't occur
            return False    #There are no Labs to remove

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

    #   cleanUpList() removes any unneeded "None" strings from the list "origList"
    #       returns the cleaned up list
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

            origList = tempListNew # set original list to this new list without "None" strings

        return origList

    #   cleanUpLabList() removes all unneeded "None" strings from this course's lab list
    #       returns the cleaned up lab list
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



    #   createLab() creates a new lab for this course
    #       returns True if lab is successfully created
    #       returns False if lab already exists
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

    #   getAllCourses()
    #       returns a list of all of the courses if there is at least one (courses.txt should exist)
    #       return None if there are no courses (courses.txt would not exist)
    def getAllCourses(self):
        fileName = self.append("application/data/courses/", "courses") + ".txt"

        if (os.path.isfile(fileName)):  # check if file exists
            file = open(fileName, "r+")
            allCourses = file.readlines()
            file.close()
            for i in range(0, allCourses.__len__()):
                allCourses[i] = allCourses[i].replace("\n","")
            return allCourses
        else:
            # There are no courses
            return None

    #   viewCourses() shows the user all of the courses and their contents
    #       if courses exist, return the string containing all the courses and their data
    #       if no courses exists, return "No courses to show"
    def viewCourses(self):

        #util = CourseUtility()

        allCourses = self.getAllCourses()

        if (allCourses == None):
            return "No courses to show"

        coursesString = ""

        for i in range(0, allCourses.__len__()):
            self.getContents(allCourses[i])
            coursesString = coursesString + self._courseName + ":\n"
            coursesString = coursesString + "Instructor= " +self._instructor +"\n"
            coursesString = coursesString + "Labs= " + str(self._labs) + "\n"
            coursesString = coursesString + "TAs= " + str(self._TAs) + "\n\n"

        return coursesString


    #   addToMasterCourseList() adds the course "courseName" to courses.txt (the file that keeps a list of all courses)
    #       returns nothing
    def addToMasterCourseList(self, courseName):

        allCourses = self.getAllCourses()

        if (allCourses == None):    # there are no courses yet  (courses.txt doesn't exist yet)
            # create courses.txt and add new course
            fileName = self.append("application/data/courses/", "courses") + ".txt"
            file = open(fileName, "+w")
            file.write(courseName)
            file.close()
        else:
            # add courseName to allCourses list
            allCourses.append(courseName)

            # write allCourses to courses.txt
            fileName = self.append("application/data/courses/", "courses") + ".txt"
            file = open(fileName, "+w")
            for i in range(0,allCourses.__len__()):
                if (i == allCourses.__len__()-1):
                    file.write(allCourses[i])
                else:
                    file.write(allCourses[i] + "\n")
            file.close()

        return

    #   removeFromMasterCourseList() removes the course "courseName" from courses.txt (the file that keeps a list of all courses)
    #       returns True if "courseName" is removed from courses.txt
    #       returns False if there are no courses to remove
    def removeFromMasterCourseList(self, courseName):

        allCourses = self.getAllCourses()

        if (allCourses == None):  # there are no courses yet  (courses.txt doesn't exist yet)

            return False    # cannot remove anything, nothing exists!

        else:

            newSize = allCourses.__len__() - 1;

            # if new size is 0, delete courses.txt because there are no courses left
            if (newSize == 0):
                fileName = self.append("application/data/courses/", "courses") + ".txt"
                os.remove(fileName)
                return True

            # create new list with new size
            newAllCourses = [None] * (newSize)
            index = 0;

            #put all courses into newAllCourses list besides "courseName" (the course to remove)
            for i in range(0,allCourses.__len__()):
                if (courseName != allCourses[i]):
                    newAllCourses[index] = allCourses[i]
                    index = index + 1

            # set allCourse to the new "newAllCourses" list
            allCourses = newAllCourses

            #write allCourses to courses.txt
            fileName = self.append("application/data/courses/", "courses") + ".txt"
            file = open(fileName, "+w")
            for i in range(0, allCourses.__len__()):
                if (i == allCourses.__len__()-1):
                    file.write(allCourses[i])
                else:
                    file.write(allCourses[i] + "\n")
            file.close()

        return True


    #   listToString() returns the list "dataList" as a string (mainly used with _labs and _TAs)
    #       returns the list "dataList" as a string
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



    #   append() is used to append two strings together
    #       In particular, this function appends a directory with a file
    #       returns the two strings "directory" and "file" as one combined string
    def append(self, directory, file):
        return directory + file


