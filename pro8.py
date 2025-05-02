day = int(input("enter the day of the week (1-4) : "))
while True:
    if day == 1:
        print("Monday")
        break
    elif day == 2:
        print("Tuesday")
        break
    elif day == 3:
        print("Wednesday")
        break
    elif day == 4:
        print("Thruesday")
        break
    else:
        print("invalid input")
        day = int(input("enter the day of the week (1-4) : "))
    
