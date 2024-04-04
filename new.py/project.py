def login():
    # Hardcoded username and password (you can replace these with your own authentication mechanism)
    username = "admin"
    password = "password"

    # Prompting user for credentials
    input_username = input("Enter your username: ")
    input_password = input("Enter your password: ")

    # Authenticating user
    if input_username == username and input_password == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Please try again.")
        # login()

if __name__ == "__main__":
    login()
