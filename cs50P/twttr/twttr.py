'''cs50p Problem set 2
a program that removes vowels from what the user inputs'''

def main():
    # prompt user for input
    text = input('Input: ').strip()
    new_txt = ''
    new_txt = shorten(text)
    # output same text with all vowels omited
    print(f'Output: {new_txt}')
# list of chars to omit
def shorten(word):
    vowel_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join(char for char in word if char not in vowel_lst)
if __name__ == "__main__":
    main()
