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
        date_outdated = (input('Date: '))
        month, day, year = date_outdated.split('/')
        number_month = months.index()
        year >= 0
        month <= 12
        day <= 31 

        if int(month) in months:
            print(year,'-',f'{month:02}','-',day)
        elif month in number_month:
            print(year,'-',f'{number_month:02}','-',day)
        else:
            pass
    except EOFError:
        print()
        break 

