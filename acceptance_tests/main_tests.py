import unittest

def main_tests():
    suite = unittest.TestSuite()

    runner = unittest.TextTestRunner()
    res = runner.run(suite)
    print(res)