"""cs50p Problemset5 testing bank.py 4/10/2023"""


def main():
    greeting  = input("Greeting: ").strip().lower()
    print(value(greeting))
    
def value(greeting):
    # greeting_hello = teller_greeting.startswith("hello")
    # greeting_h = teller_greeting.startswith("h")
    if greeting.startswith('hello') or greeting.startswith("Hello") or greeting.startswith("HeLLo"):
        return 0
    elif greeting.startswith('h'):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
