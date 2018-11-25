
from application.app import App

def main():

    user_string = ""
    app = App()
    while user_string != "quit":
        user_string = input()
        print(app.command(user_string))


if __name__ == "__main__":
    main()
