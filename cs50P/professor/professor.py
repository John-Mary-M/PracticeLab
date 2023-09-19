'''cs50p 17/09/2023 little professor'''
import random

def main():
    level = get_level()
    question_num = 1
    score = 0
    while True:
        if question_num == 10:
            break      
        x , y = generate_integer(level)
        i = 1
        while question_num < 11:   
            print(f"{x} + {y} = ", end='')
            reponse = int(input())
            if reponse != (x + y) and i != 3:
                print("EEE")
                i = i + 1
                continue
            if i == 3:
                print("EEE")
                print(f'{x} + {y} = {x + y}')
                break
            # print(f"{x} + {y} = {x + y}")
            if reponse == (x + y):
                score = score + 1
                question_num = question_num + 1
                break
        continue
        # print(x + y)
    # continue
        
    print(f'Score{score}')

def get_level():
    '''
    Gets player level, checks if its valid input and returns it
    '''
    while True:
        try:
            level = int(input("Level: "))
            while level < 4:
                match level:
                    case 1 | 2 | 3:
                        return level
                    case _:
                        break
            continue
        except ValueError:
            continue
def generate_integer(level):
    '''Generates 2 random integers(x and y) for each level'''
    match level:
        case 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        case 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        case 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        case _:
            raise ValueError
    return x, y

if __name__ == "__main__":
    main()
