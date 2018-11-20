#from CourseUtility import CourseUtility

class User:

    _courses = []
    _labs = []


    def __init__(self, firstname=None, lastname=None, username=None, password=None,
                role=None, phone=None, email=None, address=None, courses=[None], labs=[None],
                assignment=None):
        self.setName(firstname, lastname)
        self.setAccount(username, password)
        self.setRole(role)
        #self.setClass(course, lab)
        self.setCourses(courses)
        self.setLabs(labs)
        self.setInfo(phone, email, address)
        self.setAssignment(assignment)

    def setName(self, firstname, lastname):
        self.setFirstName(firstname)
        self.setLastName(lastname)

    def setFirstName(self, firstname):
        self.firstname = firstname

    def setLastName(self, lastname):
        self.lastname = lastname

    def getFirstName(self):
        if self.firstname == "None":
            return None
        return self.firstname

    def getLastName(self):
        if self.lastname == "None":
            return None
        return self.lastname

    def setAccount(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        if self.username == "None":
            return None
        return self.username

    def getPassword(self):
        if self.password == "None":
            return None
        return self.password

    def setRole(self, role):
        self.role = role

    def getRole(self):
        if self.role == "None":
            return None
        return self.role

    #Old
    #def setClass(self, course, lab):
    #    self.course = course
    #    self.lab = lab

    def setCourses(self,courses):
        self._courses = courses

    def setLabs(self,labs):
        self._labs = labs

    def getCourses(self):
        if self._courses == "None":
            return None
        return self._courses

    def getLabs(self):
        if self._labs == "None":
            return None
        return self._labs

    def setInfo(self, phone, email, address):
        self.setPhone(phone)
        self.setEmail(email)
        self.setAddress(address)

    def getInfo(self):
        return [self.getPhone(), self.getEmail(), self.getAddress()]

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, email):
        self.email = email

    def setAddress(self, address):
        self.address = address

    def getPhone(self):
        if self.phone == "None":
            return None
        return self.phone

    def getEmail(self):
        if self.email == "None":
            return None
        return self.email

    def getAddress(self):
        if self.address == "None":
            return None
        return self.address

    def setAssignment(self, assignment):
        self.assignment = assignment

    def getAssignment(self):
        if self.assignment == "None":
            return None
        return self.assignment

    def assignCourse(self, courseName):

        index = -1

        if (self._courses[0] != "None"):   #if user already has at least one course

            for i in range(0,self._courses.__len__()):    #loop through courses
                if (courseName == self._courses[i]):
                    # if they match, this user already is assigned to this course, so return
                    return False #"User already is assigned to this course"

            # user is not added to this course yet, so add them
            index = self._courses.__len__()   #set index to next spot

            # create temporary list to store new courses list
            tempCourses = [None] * (index + 1)
            for x in range(0, self._courses.__len__()):  # put contents of old list into new list
                tempCourses[x] = self._courses[x]

            tempCourses[index] = courseName

            #set selfcourses to new list
            self._courses = tempCourses
        else:

            tempCourses = [None] * (1)
            tempCourses[0] = courseName
            self._courses = tempCourses

        return True



    # remove any "None"s from the list
    def cleanUpList(self, origList):

        listName = ""

        if (origList == self._courses):
            listName = "courses"
        elif (origList == self._labs):
            listName = "labs"


        tempListOld = list(origList)
        index = 0
        newSize = tempListOld.__len__()

        for i in range(0, tempListOld.__len__()):
            if (tempListOld[i] == "None"):
                newSize = newSize - 1

        if (newSize == 0):  # if all elements in list are gone, make suer to leave one "None"
            tempListNew = ["None"] * (1)
            if (listName == "courses"):
                self._courses = tempListNew
            elif (listName == "labs"):
                self._labs = tempListNew
            return

        if (newSize != tempListOld.__len__()):
            tempListNew = [None] * (newSize)
            for i in range(0, tempListOld.__len__()):
                if (tempListOld[i] != "None"):
                    tempListNew[index] = tempListOld[i]
                    index = index + 1

            if (listName == "courses"):
                self._courses = tempListNew
            elif (listName == "labs"):
                self._labs = tempListNew


    #search through the user's courses, then remove that course if found
    def unAssignCourse(self,courseName):

        for i in range(0,self._courses.__len__()):
            if (courseName == self._courses[i]):
                self._courses[i] = "None"   # if found set to "None"

                # also remove any labs that are connected to that course
                for j in range(0,self._labs.__len__()):
                    courseLab = str(self._labs[j]).split("-")   #seperate course from lab EX: CS351-LAB801 => CS351
                    courseFromLab = courseLab[0]
                    if (courseFromLab == courseName):
                        self._labs[j] = "None"

        self.cleanUpList(self._courses)
        self.cleanUpList(self._labs)


    def assignLab(self, courseName, labName):

        # assign user to course, if not already
        self.assignCourse(courseName)

        courseLabString = courseName + "-" + labName    # example: CS351-LAB801

        index = -1

        if (self._labs[0] != "None"):  # if user already has at least one lab

            for i in range(0, self._labs.__len__()):  # loop through labs
                if (courseLabString == self._labs[i]):
                    # if they match, this user already is assigned to this lab so return
                    return False  # "User already is assigned to this lab"

            # user is not added to this lab yet, so add them
            index = self._labs.__len__()  # set index to next spot

            # create temporary list to store new labs list
            tempLabs = [None] * (index + 1)
            for x in range(0, self._labs.__len__()):  # put contents of old list into new list
                tempLabs[x] = self._labs[x]

            tempLabs[index] = courseLabString

            # set self._labs to new list
            self._labs = tempLabs
        else:

            tempLabs = [None] * (1)
            tempLabs[0] = courseLabString
            self._labs = tempLabs

    #unassign this lab form the user, if successfull, return true, otherwise return false
    def unAssignLab(self, courseName, labName):

        courseLabString = courseName + "-" + labName  # example: CS351-LAB801
        numOfCourses = 0;
        changed = False

        for i in range(0, self._labs.__len__()):
            currentCourse = str(self._labs[i]).split("-")
            currentCourse = currentCourse[0]
            if (currentCourse == courseName):
                numOfCourses = numOfCourses + 1
            if (courseLabString == self._labs[i]):
                self._labs[i] = "None"
                numOfCourses = numOfCourses - 1
                changed = True

        if (numOfCourses == 0 and changed == True):
            self.unAssignCourse(courseName)

        if (changed == False):
            return False

        self.cleanUpList(self._labs)
        return True


    def getContents(self):
        return [self.getFirstName(), self.getLastName(), self.getUsername(), self.getPassword(),
                self.getRole(), self.getPhone(), self.getEmail(), self.getAddress(),
                self.getCourses(), self.getLabs(), self.getAssignment()]
