'''cs50p problem set 3 project name: otudated 2/09/2023'''
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        user_input = input("Date: ").strip().title()
        if "/" in user_input:
            date_parts = user_input.split("/")
            month = int(date_parts[0])
            day = int(date_parts[1])
            year = int(date_parts[2])
        elif ", " in user_input:
            date_parts = user_input.split(" ")
            month, day, year = date_parts[0], date_parts[1].replace(',', ''), date_parts[2]
            # day, year = day, year
            if month in months:
                month = months.index(month) + 1
        # elif ',' not in user_input:
        #     break
        else:
            raise ValueError

        if month < 1 or month > 12 or int(day) < 1 or int(day) > 31 or int(year) < 1:
            raise ValueError

        formatted_date = f"{int(year):04d}-{month:02d}-{int(day):02d}"
        print(formatted_date)
        break
    except ValueError:
        pass
