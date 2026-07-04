import secrets


def login():
    print("===== Secure Login System =====")

    MAX_ATTEMPTS = 3
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == "admin" and password == "admin123":
            print("\nLogin Successful!")

            try:
                num1 = float(input("\nEnter first number: "))
                num2 = float(input("Enter second number: "))
                print("Sum:", num1 + num2)
            except ValueError:
                print("Invalid numbers.")
            session_token = secrets.token_hex(16)
            print("Session Token:", session_token)

            return

        else:
            attempts += 1
            print(f"\nInvalid username or password. Attempts remaining: {MAX_ATTEMPTS - attempts}")

    print("\nToo many failed login attempts. Access denied.")


login()