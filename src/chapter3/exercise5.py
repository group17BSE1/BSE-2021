try:  # the block below is executed whenever the expected entry is input.
    g = int(input("enter no of guests>>"))
    if 0 < g <= 50:
        print("$4000")
    elif 50 < g <= 100:
        print("$10000")
    elif 100 < g <= 200:
        print("$15000")
    elif g > 200:
        print("$20000")
except:
    print("INVALID ENTRY PLEASE")  # This is an error message printed whenever wrong entry is input
