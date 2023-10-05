'''cs50p vanity plates:
In Massachusetts, home to Harvard University, it’s possible
to request a vanity license plate for your car, with your
choice of letters and numbers instead of random ones. Among
the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters
(letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must
come at the end. For example, AAA222 would be an acceptable …
vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity
plate and then output Valid if meets all of the requirements or Invalid
if it does not. Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets
all requirements and False if it does not. Assume that s will be a str.
You’re welcome to implement additional functions for is_valid to call
(e.g., one function per requirement).
'''

def main():
    '''Entry point'''
    # Prompt the user to enter a vanity plate
    plate = input("Plate: ").strip().upper()
    # plate = remove_punctuation(plate)
    # print(plate)
    if is_valid(plate):  # Check if the entered plate is valid
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    '''checks for valid plate'''
    # Check if the length of the plate is within the valid range
    if len(s) < 2 or len(s) > 6:
        return False
    # Check if plates starts with at least 2 letters
    if not s[:2].isalpha():
        return False
    # Check if the first number used is '0'
    if s[2:].isdigit() and s[2] == '0':
        return False

    # Check if there are numbers in the middle of the string
    found_digit_after_letter = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            found_digit_after_letter = True
        elif found_digit_after_letter:
            return False

    # Check for any invalid characters or punctuation marks
    if any(char in ['.', ',', ' ', '?', '!'] for char in s):
        return False

    return True


if __name__ == "__main__":
    main()
 