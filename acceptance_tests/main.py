import unittest
from supervisor_assign_lab import TestSupAssignTALab

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestSupAssignTALab))

runner = unittest.TextTestRunner()
res=runner.run(suite)
print(res)