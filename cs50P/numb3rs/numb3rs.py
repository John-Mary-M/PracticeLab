"""cs50p problemset 7 30/10/2023 numb3rs.py"""
import sys
import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validates IPV4 IP address"""
    # ip = sys.argv(1)
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]$", ip):
        lst_prts_ip = ip.split(".")
        for prt in lst_prts_ip:
            if int(prt) < 0 or int(prt) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
