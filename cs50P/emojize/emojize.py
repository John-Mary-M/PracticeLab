"""cs50p 12/09/2023 problemset 4 emojize"""
import emoji

try:
    usr_str = input("Input: ").lower().strip()
    usr_str = emoji.emojize(usr_str, language='alias')
    print('Output:', usr_str)
except IndexError:
    pass
