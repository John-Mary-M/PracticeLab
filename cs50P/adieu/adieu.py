'''cs50p 13/09/2023 problemset 4 adieu.py'''
import inflect
import sys

# Create an instance of the inflect engine
p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        if not name:
            break
        names.append(name)
    except EOFError:
        print()
        break
n = len(names)
if n == 1:
    farewell = f"Adieu, adieu, to {p.join(names, ', ')}"
else:
    farewell = f"Adieu, adieu, to {p.join(names, ',')}"

print(farewell)
sys.exit(0)
