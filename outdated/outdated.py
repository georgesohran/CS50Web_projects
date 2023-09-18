month =[
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
        ordate = input().replace(" ","")
        month,day,year = ordate.split("/")
        month,day,year = int(month),int(day),int(year)
        break
    except ValueError:
        for m in month:
            if ordate.startswith(m):
                month = month.index(m)+1
                ordate.replace(m,"")
                day,year = ordate.split(",")
                break
    except EOFError:
        pass


print(f"{year}-{month:02}-{day:02}")