"""pytests for jar.py cookie jar problem"""
from jar import Jar


def main():
    """Entry Point"""
    test_init()
    test_deposit()

def test_init():
    '''Tests class initializer'''
    jar =Jar()
    assert jar._capacity == 12

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    '''Tests class functionality to add cookies to the jar'''
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8

def test_withdraw():
    '''Tests class functionality to withdraw cookies'''
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4
if __name__ == "__main__":
    main()
