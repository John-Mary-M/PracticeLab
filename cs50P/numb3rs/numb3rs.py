"""cs50p problemset 7 30/10/2023 numb3rs.py"""
import sys
import re


def main():
    """Entry point"""
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validates IPv4 IP address"""
    match = re.search(r"^(\d{1,3}\.){3}\d{1,3}$", ip)
    if match:
        lst_prts_ip = ip.split(".")
        for prt in lst_prts_ip:
            if 0 <= int(prt) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
