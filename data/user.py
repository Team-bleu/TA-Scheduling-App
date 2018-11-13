

class User:
    def __init__(self, firstname=None, lastname=None, username=None, password=None,
                role=None, phone=None, email=None, address=None, course=None, lab=None,
                assignment=None):
        self.setName(firstname, lastname)
        self.setAccount(username, password)
        self.setRole(role)
        self.setClass(course, lab)
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

    def setClass(self, course, lab):
        self.course = course
        self.lab = lab

    def getCourse(self):
        if self.course == "None":
            return None
        return self.course

    def getLab(self):
        if self.lab == "None":
            return None
        return self.lab

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

    def getContents(self):
        return [self.getFirstName(), self.getLastName(), self.getUsername(), self.getPassword(),
                self.getRole(), self.getPhone(), self.getEmail(), self.getAddress(),
                self.getCourse(), self.getLab(), self.getAssignment()]
