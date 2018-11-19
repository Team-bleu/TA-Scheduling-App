from tests.sprint1_acceptance_test import main_tests
import mainUnitTests
from app import App


def main():

    # This boolean is to see if we want
    # to check the acceptance tests
    # and unittests
    test = False # set this to true to run acceptance test
    unittest = False # set this to true to run unit test


    # Limitation for unittest and acceptance test: Since we don't have remove command, you need to manually
    # delete files to make sure both unittest and acceptence tests are passing when we run them multiple times
    # will fix this in sprint two

    if unittest:
        print("start unit tests.\n")
        mainUnitTests.main_tests()
        print("Finished unit tests.\n")

    if test:
        print("\nstart acceptance tests.\n")
        main_tests.main_tests()
        print("\nFinished acceptance tests.\n")

    print("\nWelcome to TA Scheduling App\n")
    user_string = ""
    app = App()
    while user_string != "quit":
        user_string = input()
        print(app.command(user_string))


if __name__ == "__main__":
    main()
