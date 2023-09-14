def caught_speeding(speed, bday):
    if bday == True:
        speed = speed - 5
    if speed <= 60:
            print("No challan")
    elif speed <= 80:
            print("Small challan")
    elif speed > 80:
            print("Heavy challan")
    else:
        print("Invalid speed")
caught_speeding(81, True)
caught_speeding(81, False)