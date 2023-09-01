"""cs50p 23/08/2023
    loops"""
# i = 0
# while i < 3:
#     print('meow')
#     i += 1

# for i in [0, 1, 2]:
#     print('meow')

# for i in range(3):
#     print('meow')

# for _ in range(3):
#     print('meow')


def main():
    """entry point"""
    number = get_number()
    meow(number)


def get_number():
    """gets a number from the user"""
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


def meow(x):
    """meows x time"""
    # while True:
    #     x = int(input('What\'s x? '))
    # if x > 0:
    #     return x

    for _ in range(x):
        print("meow")


if __name__ == "__main__":
    main()
