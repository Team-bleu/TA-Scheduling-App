
from user import User

class BSTUtility:


    _user = None;
    _root = None;
    _current = None;
    _parent = None;
    _leftChild = None;
    _rightChild = None;
    _currentFile = None;

#    def __init__(self):
#        pass


    def getRoot(self):
        rootFile = ""
        rootFile = open("root.txt", "r+")
        rootName = rootFile.readlines()
        rootFile = rootName[0]
        currentFile = rootFile
        print(rootFile)
        print(rootName)
        print(currentFile)

    def getUser(self, username):
        pass
        #if (_currentFile == username):
        #    return _currentFile
        #else:
        #    if (username < _currentFile):
               # _current = _current.leftChild

    def openCurrent(self):
        file = open(self._currentFile, "r+")
        rfile = file.readlines()
        _current = User(rfile[0], rfile[1], rfile[2], rfile[3], rfile[4],
                        [rfile[5], rfile[6], rfile[7]], rfile[8], rfile[9], rfile[10],
                        rfile[11], rfile[12], rfile[13])
        print(_current)
        self._parent = getParent()          #getContents(_current.getParent())
        self._leftChild = getLeftChild()   #getContents(_current.getLeftChild())
        self._rightChild = getRightChild() #getContents(_current.getRightChild())

    def getLeft(self):
         pass#_current




obj = BSTUtility()
obj.getRoot()
obj.openCurrent(obj._current)