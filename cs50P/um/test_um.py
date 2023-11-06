"""pytests for um.py"""
from um import count

def main():
    '''testing'''
    test_uppercase_um()
    test_lowercase_um()
    
def test_uppercase_um():
    """checks if count ignore uppercase um"""
    assert count("UM") == 0
    
def test_lowercase_um():
    '''verifys that count takes lowercase um'''
    assert count("um") == 1
    
def test_um_word():
    '''checks if um ignores occurence in the middle of another word'''
    assert count('yummy') == 0
if __name__=="__main__":
    main()
