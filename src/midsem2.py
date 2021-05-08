while True:
    code = input("enter customer's code :")
    if code == 'r' or code == 'i' or code == 'c':
        while True:
            try:
                begin = int(input("enter beginning meter reading:"))
                if 0 <= begin <= 999999999:
                    break
                else:
                    print("enter a positive value with not more than nine digits ")
            except:
                print("Write a numerical value")
        while True:
            try:
                end = int(input("enter ending meter reading:"))
                if 0 <= end <= 999999999:
                    break
                else:
                    print("enter positive integer with not more than nine digits")
            except:
                print("write a numerical value")
    else:
        print('invalid code')
        break
    if end > begin:
        gallons_of_water = (end - begin) / 10
    else:
        gallons_of_water = ((1000000000 - begin) + end) / 10
    if code == 'r':
        bill = (0.0005 * gallons_of_water) + 5.00
    elif code == 'c':
        extra = gallons_of_water - 4000000
        if gallons_of_water <= 4000000:
            bill = 1000.00
        elif gallons_of_water > 4000000:
            bill = (extra * 0.00025)
    elif code == 'i':
        more = gallons_of_water - 10000000
        if gallons_of_water <= 4000000:
            bill = 1000.00
        elif 4000000 < gallons_of_water <= 10000000:
            bill = 2000.00
        elif gallons_of_water > 10000000:
            bill = (extra * 0.00025) + 2000.0
    print(
        f"The customer's code: {code} \nThe customer's beginning meter reading: {begin} \nThe customer's ending meter reading: {end} \nThe gallons of water used: {gallons_of_water}  \nAmount of money billed to the customer: ${bill:.2f} ")
