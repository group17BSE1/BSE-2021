# this program prompts the user for the rate and hours worked and prints the pay.
hours = input("Enters hours:")  # this is to prompt the user for hours worked
rate = input("Enters rate:")  # this prompts the user to enter the rate payable per hour.


def compute_pay(h, r):
    try:
        h = float(hours)  # this converts the hours input to a float
        r = float(rate)  # this converts the rate input to a float
        if h <= 40:
            pay = float(h * r)  # this is the pay for hours of work below or equal to 40
        else:
            pay = float(r * 40 + (1.5 * r * (h - 40)))  # this is the pay for hours of work above forty.
        return pay
    except ValueError:
        return "please enter numeric input"  # this returns an error message whenever non numeric input is entered.


pay = compute_pay(hours, rate)
print(pay)
