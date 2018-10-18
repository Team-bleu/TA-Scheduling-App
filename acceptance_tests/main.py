import unittest
from supervisor_assign_lab import TestSupAssignTALab
from supervisor_create_account import TestSupCreateAccount

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSupAssignTALab))
suite.addTest(unittest.makeSuite(TestSupCreateAccount))

runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)