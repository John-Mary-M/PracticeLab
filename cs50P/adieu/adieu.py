'''cs50p 13/09/2023 problemset 4 adieu.py'''
while True:
    try:
        usr_input = input("Name: ")
        if ' ' in usr_input:
            lst_names = usr_input.split(' ')
            for name in lst_names[ : -1]:
                name = name + ', '
                print(f'Adieu, adieu, to {name}')
        else:
            print(f'Adieu, adieu, to {name}')
    except EOFError:
        break