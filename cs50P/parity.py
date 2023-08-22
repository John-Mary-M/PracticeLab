"""cs50p 22/08/2023
    parity with modulo
"""


def main():
    """Checks for even number"""
    x_num = int(input("What is x? "))
    if is_even(x_num):
        print("Even")
    else:
        print("Odd")


def is_even(n_num):
    """returns true if n is even"""
    return n_num % 2 == 0

main()
