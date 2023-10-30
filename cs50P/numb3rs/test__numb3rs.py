"""pytest for validate(ip) in numb3rs.py"""
from numb3rs import validate


def main():
    test_range()


def test_range():
    """Tests ipv4 range"""
    assert validate("192.168.0.3")
    assert validate("1.2.3.4")


def test_invalid_range2():
    """tests invalid range"""
    assert validate("279.198.4587.3") is False


if __name__ == "__main__":
    main()
