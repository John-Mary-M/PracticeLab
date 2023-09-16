'''cs50p 16/09/2023 game.py a guess the number game'''
import random
while True:
    try:
        n = int(input("Level: "))
        if n < 0:
            continue
        gen_num = random.randint(1, n)
        
        while True:
            # prompt for another guess each a wrong guess is entered
            # until player finds the right number
            player_guess = int(input('Guess: '))
            if player_guess < gen_num:
                print('Too small!')
                continue
            elif player_guess > gen_num:
                print('Too large!')
                continue
            else:
                print('Just right!')
                break
        break
        
    except (ValueError, TypeError):
        pass
    