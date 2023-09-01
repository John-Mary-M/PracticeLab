"""cs50p 24/08/2023"""
def main():
    '''entry point'''
#     print_column()
#     print_row(4)

# def print_column():
#     '''prints 3 block obstacle'''
#     for _ in range(3):
#         print('#')

# def print_row(width):
#     '''prints row of obstacles'''
#     print("?" * width)
    print_square(3)

def print_square(size):
    """prints 2d square"""
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            print('#', end='')
        print()
main()
