import main_tests
from app import App


def main():

    # This boolean is to see if we want
    # to check the acceptance tests
    test = False
    if test:
        main_tests.main_tests()
        print("Finished acceptance tests.")

    user_string = ""
    app = App()
    while user_string != "quit":
        user_string = input()
        app.command(user_string)


if __name__ == "__main__":
    main()
