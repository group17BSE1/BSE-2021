try:  # this tries to run the blocks below whenever the user enters the expected format of input.
    p = float(input("Enter hours:"))
    s = float(input("Enter rate:"))
    pay = (p * s)
    w = (1.5 * s * p)
    if p <= 40:
        print(pay)  # This prints the pay for hours entered from forty and below.

    else:
        print(w)  # This prints the extra pay for whoever works for more than 40 hours
except:
    print("please enter numeric input")  # This will print an error message when the user enters  non-numeric input.
