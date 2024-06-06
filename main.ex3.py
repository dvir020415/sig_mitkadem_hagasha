import string


# Base class for custom exceptions related to the blog
class BlogException(Exception):
    pass


# Exception for illegal characters in the username
class UsernameContainsIllegalCharacter(BlogException):
    def __init__(self, illegal_char):
        self.illegal_char = illegal_char

    def __str__(self):
        return f"The username contains illegal character: {self.illegal_char}"


# Exception for too short usernames
class UsernameTooShort(BlogException):
    def __str__(self):
        return "The username too short"


# Exception for too long usernames
class UsernameTooLong(BlogException):
    def __str__(self):
        return "The username too long"


# Exception for missing character types in the password
class PasswordMissingCharacter(BlogException):
    def __init__(self, missing_char):
        self.missing_char = missing_char

    def __str__(self):
        return f"password missing a character: {self.missing_char}"


# Exception for too short passwords
class PasswordTooShort(BlogException):
    def __str__(self):
        return "The password is too short"


# Exception for too long passwords
class PasswordTooLong(BlogException):
    def __str__(self):
        return "The password is too long"


# Function to check the validity of the username and password
def check_input(username, password):
    # Check if the username is too short
    if len(username) < 3:
        raise UsernameTooShort()

    # Check if the username is too long
    if len(username) > 16:
        raise UsernameTooLong()

    # Check for illegal characters in the username
    if any(char not in string.ascii_letters + string.digits + "_" for char in username):
        illegal_char = next((char for char in username if char not in string.ascii_letters + string.digits + "_"), None)
        raise UsernameContainsIllegalCharacter(illegal_char)

    # Dictionary to track required character types in the password
    required_chars = {
        "Uppercase": False,
        "Lowercase": False,
        "Digit": False,
        "Special": False
    }

    # Check each character in the password for required types
    for char in password:
        if char.isupper():
            required_chars["Uppercase"] = True
        elif char.islower():
            required_chars["Lowercase"] = True
        elif char.isdigit():
            required_chars["Digit"] = True
        elif char in string.punctuation:
            required_chars["Special"] = True

    # Collect missing character types
    missing_chars = [char_type for char_type, present in required_chars.items() if not present]
    if missing_chars:
        raise PasswordMissingCharacter(", ".join(missing_chars))

    # Check if the password is too short
    if len(password) < 8:
        raise PasswordTooShort()

    # Check if the password is too long
    if len(password) > 40:
        raise PasswordTooLong()

    print("OK")  # Indicate that the input is valid


# Main function to run test cases and prompt user for input
def main():
    test = [
        ("1", "2"),
        ("0123456789ABCDEFG", "2"),
        ("A_a1.", "12345678"),
        ("A_1", "2"),
        ("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary"),
        ("A_1", "abcdefghijklmnop"),
        ("A_1", "ABCDEFGHIJLKMNOP"),
        ("A_1", "ABCDEFGhijklmnop"),
        ("A_1", "4BCD3F6h1jk1mn0p"),
        ("A_1", "4BCD3F6.1jk1mn0p")
    ]

    # Run test
    for username, password in test:
        try:
            check_input(username, password)
        except BlogException as e:
            print(e)

    # Prompt user for input until valid credentials are provided
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter password: ")
            check_input(username, password)
            break
        except BlogException as e:
            print(e)


if __name__ == "__main__":
    main()
