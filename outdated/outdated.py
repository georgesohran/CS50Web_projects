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

def format_check1(s):
    try:
        a,b,c = s.split("/")
    except ValueError:
        return False
    else:
        return True

def format_check2(s):
    if s.has()

while True:
    ordate = input("Date: ").replace(" ","")
    try:
        month1,day,year = ordate.split("/")
        month1,day,year = int(month1),int(day),int(year)
    except ValueError:
        for m in month:
            if ordate.startswith(m):
                month1 = month.index(m)+1
                ordate = ordate.replace(m,'')
                day,year = ordate.split(",")
                day,year = int(day),int(year)
                break
    except EOFError:
        break

    if (0<month1<=12) and (0<day<=31):
        print(f"{year}-{month1:02}-{day:02}")
        break
    else:
        pass



