"""cs50p 12/09/2023 FIGLET problemset 4"""
import sys
from sys import argv
# from sys import exit
# from inspect import isfunction
import pyfiglet

def main():
    '''Entry point'''
    if len(sys.argv) != 3:
        # figlet.getFonts()
        # print(figlet.renderText(usr_str))
        sys.exit("Invalid usage")
    
    if ".py" not in sys.argv[0]:
        sys.exit("Invalid usage")

    if len(argv) > 1:
        # figlet.setFont(font=f)
        figlet = pyfiglet.Figlet()
        fnts = figlet.getFonts()
        if '-f' in sys.argv[1] or '--font' in sys.argv[1]:
            usr_str = input("Input: ").strip()
            print(pyfiglet.figlet_format(usr_str, argv[2]))
            if sys.argv[2] not in fnts:
                print("font issue")
                sys.exit("Invalid usage")
            
        else:
            # print(sys.argv[1])
            sys.exit("Invalid usage")
    # else:
    #     figlet.setFont(font='slant')
    #     print(figlet.renderText(usr_str))
main()
