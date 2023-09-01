def main():
    '''
        Entry point
    '''
    # Prompt the user to enter a vanity plate
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):  # Check if the entered plate is valid
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    '''checks for valid plate'''
    # Check if the length of the plate is within the valid range
    if len(s) < 2 or len(s) > 6:
        return False
    # check if plates starts with at least 2 letters
    if not s[:2].isalpha():
        return False
    # Check if any number used is a 0 after the second character
    if any(char.isdigit() and char == '0' for char in s[2:]):
        return False
    # Check for any invalid characters or punctuation marks
    for item in s:
        if item in ['.', ',', ' ', '?', '!']:
            return False
    return True

main()
