""" the program will compute and display the amount of money which the customer will be
 billed for water usage during the current billing period after the user enters
 the customer code,beginning and ending meter reading"""


def gallons(a, b):  # this function accepts two variables
    if b > a:
        gallon = (b - a) / 10
        print("Gallons of water used: ", gallon)
        # for the case beginning meter reading is less than ending meter reading
    else:
        a = 1000000000 - a

        gallon = (a + b) / 10
        print("Gallons of water used: ", gallon)
    return gallon


while True:
    code = input("Enter code: ")  # prompt customer for  code
    if code.lower() == "r":
        # prompt user to enter the meter readings
        a = int(input("Enter beginning meter reading: "))
        b = int(input("Enter ending meter reading: "))
        if (0 <= a <= 999999999) and (0 <= b <= 999999999):
            print("Customer code: ", code)

            print(f"Beginning meter reading: {a:09d} ")
            print(f"Ending meter reading: {b:09d} ")
            gallon = gallons(a, b)
            bill = 5.00 + (gallon * 0.0005)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            # error message printed when reading out of range is entered
            print("Meter reading not in range!\n")
    elif code.lower() == "c":
        a = int(input("Enter beginning meter reading: "))
        b = int(input("Enter ending meter reading: "))
        if (0 <= a <= 999999999) and (0 <= b <= 999999999):
            print("Customer code: ", code)
            print(f"Beginning meter reading: {a:09d} ")
            print(f"Ending meter reading: {b:09d} ")
            gallon = gallons(a, b)
            if gallon <= 4000000.00:
                bill = 1000.00
            else:
                bill = 1000.00 + ((gallon - 4000000) * 0.00025)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            # error message printed when reading out of range is entered
            print("Meter reading not in range!\n")
    elif code.lower() == "i":
        a = int(input("Enter beginning meter reading: "))
        b = int(input("Enter ending meter reading: "))
        if (0 <= a <= 999999999) and (0 <= b <= 999999999):
            print("Customer code: ", code)
            print(f"Beginning meter reading: {a:09d} ")
            print(f"Ending meter reading: {b:09d} ")
            gallon = gallons(a, b)
            if gallon <= 4000000:
                bill = 1000.00
            elif 4000000 < gallon <= 10000000:
                bill = 2000.00
            else:
                bill = 2000 + ((gallon - 10000000) * 0.00025)
            print(f"Amount billed: ${bill:.2f}\n")
        else:
            print("Meter reading not in range!\n")
    else:
        break
