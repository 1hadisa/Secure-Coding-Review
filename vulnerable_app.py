import os
import random

def login():
    print("===== Login System =====")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "admin123":
        print("\nLogin Successful!")

        expression = input("\nEnter a math expression: ")
        print("Result:", eval(expression))

        command = input("\nEnter a system command: ")
        os.system(command)

        session_token = random.randint(100000, 999999)
        print("Session Token:", session_token)

    else:
        print("\nInvalid username or password.")

login()