import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    tfrom , tto = s.split(" to ")
    match1 = re.search(r"([0-9]{1,2})\:?([0-9]{1,2})?\ (AM?|PM?)",tfrom)
    match2 = re.search(r"([0-9]{1,2})\:?([0-9]{1,2})?\ (AM?|PM?)",tto)
    if match1 and match2:
        hours1, mins1 = int(match1.group(1)), match1.group(2)
        APM1  = match1.group(3)
        hours2, mins2 = int(match2.group(1)), match2.group(2)
        APM2  = match2.group(3)

        if APM1 == "PM":
            if hours1 == 12:
                pass
            else:
                hours1 += 12
        elif hours1 == 12:
                hours1 = 0

        if APM2 == "PM":
            if hours2 == 12:
                pass
            else:
                hours2 += 12
        elif hours2 == 12:
                hours2 = 0

        if mins1 == None:
            mins1 = 0
        else:
            mins1 = int(mins1)
            if mins1 >= 60:
                raise ValueError
        if mins2 == None:
            mins2 = 0
        else:
            mins2 = int(mins2)
            if mins2 >= 60:
                raise ValueError
    else:
        raise ValueError


    return f"{hours1:02}:{mins1:02} to {hours2:02}:{mins2:02}"




if __name__ == "__main__":
    main()