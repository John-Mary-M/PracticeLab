'''cs50p bitcoin.py 19/09/2023'''
import sys
# import json
import requests


def main():
    '''entry point'''
    bitcoin = get_user_input()
    print(bitcoin)
    x = bitcoin_rate()
    dollars = (x * bitcoin)
    print(f'${dollars:,.4f}')

def get_user_input():
    '''gets the user input from the commandline'''
    if len(sys.argv) < 2:
        print("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
        print(type(amount))
        return amount

    except (ValueError, TypeError, IndexError):
        if ValueError or TypeError:
            print('command-line arguement is not a number')
        elif IndexError:
            print('Missing command-line arguement')

def bitcoin_rate():
    '''coverts user input to equvalent bitcoins using the coin desk API'''
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        price_usd = float(data["bpi"]["USD"]["rate"].replace(",", ""))
        return price_usd
    except requests.exceptions.RequestException:
        print("Failed to retrieve the Bitcoin price. Please try again later.")
        sys.exit(1)
    except (KeyError, ValueError):
        print("Failed to parse the API response. Please try again later.")
        sys.exit(1)

if __name__ == "__main__":
    main()
    