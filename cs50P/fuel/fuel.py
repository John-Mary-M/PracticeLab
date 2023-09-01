"""cs50p problem set 3 31/08/2023 Fuel Guage project"""
while True:
    # print(f'{type(numerator)}, {type(denominator)}')
    try:
        numerator, denominator = input("Faction: ").split("/")
        numerator, denominator = int(numerator), int(denominator)
        if numerator > denominator or denominator == 0:
            continue
        fuel_level = ((numerator) / (denominator)) * 100
        match fuel_level:
            case 100 | 99:
                print("F")
                break
            case 0|1:
                print("E")
                break
            case _:
                print(f"{fuel_level:.0f}%")
                break
    except (ValueError, ZeroDivisionError):
        pass
