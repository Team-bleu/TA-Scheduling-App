

class User:
    def __init__(self, firstname="None", lastname="None", username="None", password="None",
                role="None", information="None", course="None", lab="None",
                assignment="None", parent="None", leftChild="None", rightChild="None"):
        self.setName(firstname, lastname)
        self.setAccount(username, password)
        self.setRole(role)
        self.setClass(course, lab)
        self.setInfo(information)
        self.setAssignment(assignment)
        self.setParent(parent)
        self.setLeftChild(leftChild)
        self.setRightChild(rightChild)

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

    def setAssignment(self, assignment):
        self.assignment = assignment

    def getAssignment(self):
        return self.assignment

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setLeftChild(self, leftChild):
        self.leftChild = leftChild

    def getLeftChild(self):
        return self.leftChild

    def setRightChild(self, rightChild):
        self.rightChild = rightChild

    def getRightChild(self):
        return self.rightChild

    def getContents(self):
        return [self.getFirstName(), self.getLastName(), self.getUsername(), self.getPassword(), self.getRole(),
                self.getInfo(), self.getCourse(), self.getLab(), self.getAssignment(),
                self.getParent(), self.getLeftChild(), self.getRightChild()]
