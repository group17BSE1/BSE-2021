try:
    g = input("Enter job location")
    b = int(input("Enter pay"))
    # ".upper" changes the whatever format of the location to uppercase
    if g.upper() == "MBARARA" and b <= 4000000:
        print("No Thanks, i can find something better")
    elif g.upper() == "MBARARA" and b > 4000000:
        print("i can work with this")
    elif g.upper() == "KAMPALA" and b >= 10000000:
        print("I can work with this")
    elif g.upper() == "KAMPALA" and b < 10000000:
        print("No Thanks, I can find something better")
    elif g.upper() == "SPACE" and b >= 0:
        print("Without doubt i will work")
    elif b >= 6000000:
        print('i will surely work')
    else:
        print("NO THANKS")  # The string is printed whenever pay below the minimum pay for all other locations is entered

except:
    print('INVALID ENTRY PLEASE')  # prints an error message whenever wrong input is entered
