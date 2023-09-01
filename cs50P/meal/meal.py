"""cs50p 23/08/2023 problem set 1"""


def main():
    """runs the program"""
    time = input("What is it? ")
    time = convert(time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print('lunch time')
    elif time >= 18.0 and time <= 19.0:
        print('dinner time')

def convert(time):
    """Converts time str to the corresponding
    number of hours as a float e.g time like "7:30"
    should return 7.5
    """
    # time = input("What is it? ")
    hour, minute = time.split(":")
    hour = float(hour.strip())
    minute = float(minute.strip())

    # convert miutes
    minute = minute / 60

    # return hour.minute
    return hour + minute


main()
