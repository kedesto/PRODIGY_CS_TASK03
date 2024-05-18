import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~`]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, special_char_error]
    error_msgs = ["Password must be at least 8 characters long.", "Password must contain at least one digit.",
                  "Password must contain at least one uppercase letter.", "Password must contain at least one lowercase letter.",
                  "Password must contain at least one special character (!,@,#,$, etc.)"]

    strength = len(errors) - sum(errors)
    if strength == len(errors):
        return "Your password is weak. " + ", ".join(error_msgs)
    elif strength == len(errors) - 1:
        return "Your password is medium. " + error_msgs[errors.index(True)]
    else:
        return "Your password is strong."

# Test the function
password = input("Enter your password: ")
print(check_password_strength(password))
