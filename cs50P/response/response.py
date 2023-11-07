"""cs50p problemset 7 7/11/2023 prompts the user for an email 
    address via input and then prints Valid or Invalid, respectively, 
    if the input is a syntatically valid email address. 
    You may not use re. And do not validate whether the email address’s 
    domain name actually exists
"""

from validator_collection import validators, checkers, errors


def main():
    """Entry Point"""
    print(validated(input("What's your email address? ")))


def validated(s):
    """validates user input using validator collection"""
    try:
        s = validators.email(s)
        # print(s)
        return "Valid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()
