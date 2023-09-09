"""cs50p 3/09/2023 problemset 3 grocery list"""
grocery_dict = {}
# grocery_list = []
# num = 0
while True:
    try:
        list_item = input().strip().upper()
        if list_item == "":
            continue
        if "AND" in list_item:
            items = list_item.split("AND")
            for item in items:
                item = item.strip()
                grocery_dict[item] = grocery_dict.get(item, 0) + 1
        else:
            grocery_dict[list_item] = grocery_dict.get(list_item, 0) + 1
    except (EOFError, TypeError):
        print()
        sorted_grocery = sorted(grocery_dict.items(), key=lambda x: x[0])

        for item, count in sorted_grocery:
            print(f"{count} {item}")
        break
