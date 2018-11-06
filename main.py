from tests.sprint1_acceptance_test import main_tests
import mainUnitTests
from app import App


def main():

    # This boolean is to see if we want
    # to check the acceptance tests
    # and unittests
    test = True # set this to true to run acceptance test
    unittest = True # set this to true to run unit test

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
