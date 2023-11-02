"""pytest for validate(ip) in numb3rs.py"""
import subprocess
from numb3rs import validate


def main():
    test_range()
    test_invalid()
    test_firstByte_in_range()
    test_exit_code()

def test_range():
    """Tests ipv4 range"""
    assert validate("192.168.0.3") is True
    assert validate("255.255.255.255") is True

def test_firstByte_in_range():
    """checks octets with one digit"""
    assert validate("192.278.3258.496") is False

def test_invalid_range2():
    """tests invalid range"""
    assert validate("279.198.458.278") is False

def test_firstByte_out_of_range():
    """Tests only the first byte of IPv4 address is in range"""
    assert validate("256.168.0.3") is False


if __name__ == "__main__":
    main()
