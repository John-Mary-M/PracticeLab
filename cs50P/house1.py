'''cs50p 22/08/2023
    more on conditionals: The match and case
'''
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Dreco":
        print("Slytherin")
    case _:
        print("Who?")
        