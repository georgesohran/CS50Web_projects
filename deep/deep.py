a = input()

match a :
    case str(42)|"Forty Two"|"forty-two"|"forty two"|"Forty two":
        print("Yes")
    case _:
        print("No")