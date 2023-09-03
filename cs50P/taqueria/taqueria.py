"""cs50p problemset 3 1/09/2023 taqueria
EOF or ctrl-d was not working properly as required by the question simply because
am working on a windows system locally. However the same code on a linux system
works perfectly
"""

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}
total_order = 0.0
while True:
    try:
        order = input("item: ").title().strip()
        if order == "":
            continue
        if order not in menu:
            continue
            # print(f'Total: ${menu[order]:.2f}')
        total_order = total_order + menu[order]
        print(f"Total: ${total_order:.2f}")
    except (ValueError, TypeError, EOFError, KeyError):
        break
