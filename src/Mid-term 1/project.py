""" the program will compute and display the amount of money which the customer will be
 billed for water usage during the current billing period after the user enters
 the customer code,beginning and ending meter reading"""
code = input("Enter code: ")
meter_reading1 = input("Enter beginning meter reading: ")
meter_reading2 = input("Enter ending meter reading: ")


def gallons(meter_reading1, meter_reading2):  # this function accepts two variables
    if meter_reading2 > meter_reading1:
        gallon = (meter_reading2 - meter_reading1) / 10
        print("Gallons of water used: ", gallon)
    else:
        meter_read1 = 1000000000 - meter_reading1

        gallon = (meter_reading2 + meter_reading1) / 10
        print("Gallons of water used: ", gallon)
    return gallon
