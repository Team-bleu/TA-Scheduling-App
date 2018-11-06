from tests.sprint1_acceptance_test import main_tests
import mainUnitTests
from app import App


def main():

    # This boolean is to see if we want
    # to check the acceptance tests
    # and unittests
    test = True
    unittest = False
    if test:
        main_tests.main_tests()
        print("Finished acceptance tests.")
    if unittest:
        mainUnitTests.main_tests()
        print("Finished unit tests.")

    user_string = ""
    app = App()
    while user_string != "quit":
        user_string = input()
        print(app.command(user_string))


if __name__ == "__main__":
    main()
