'''cs50p 16/09/2023 game.py a guess the number game'''
import random
while True:
    try:
        n = int(input("Level: "))
        if n < 0:
            continue
        gen_num = random.randint(1, n)
        
        for guess in range(gen_num):
            player_guess = int(input('Guess: '))

            if player_guess < gen_num:
                print('Too small!')
                guess =+ 1
                continue
            elif player_guess > gen_num:
                print('Too large!')
                guess =+ 1
                continue
            else:
                print('Just right!')
                break
        break
        
    except (ValueError, TypeError):
        pass
    