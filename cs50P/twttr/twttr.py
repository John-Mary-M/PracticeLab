'''cs50p Problem set 2
a program that removes vowels from what the user inputs'''

def main():
    # prompt user for input
    text = input('Input: ').strip()
    new_txt = ''
    new_txt = remove_vowels(text)
    # output same text with all vowels omited
    print(f'Output: {new_txt}')
# list of chars to omit
def remove_vowels(text):
    vowel_lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join(char for char in text if char not in vowel_lst)
main()
