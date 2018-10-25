

class User:

    def __init_(self, firstname=None, lastname=None, username=None, password=None,
                logged=False, role=None, course=None, lab=None, information=None):
        self.setName(firstname, lastname)
        self.setAccount(username, password)
        self.setLogged(logged)
        self.setRole(role)
        self.setClass(course, lab)
        self.setInfo(information)

    def setName(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getFirstName(self):
        return self.firstname

    def getLastName(self):
        return self.lastname

    def setAccount(self, username, password):
        self.username = username
        self.password = password

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def setLogged(self, logged):
        self.logged = logged

    def getLogged(self):
        return self.logged

    def setRole(self, role):
        self.role = role

    def getRole(self):
        return self.role

    def setClass(self, course, lab):
        self.course = course
        self.lab = lab

    def getCourse(self):
        return self.course

    def getLab(self):
        return self.lab

    def setInfo(self, information):
        self.information = information

    def getInfo(self):
        return self.information
