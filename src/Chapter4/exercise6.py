# this program computes the pay for workers according to the hours worked.
h = float(input("Enters hours:"))  # this is to prompt the user for hours worked
r = float(input("Enters rate:"))  # this prompts the user to enter the rate payable per hour.


def compute_pay(h, r):
    if h <= 40:
        pay = (h * r)  # this is the pay for hours of work below or equal to 40
    else:
        pay = (r * 40 + (1.5 * r * (h - 40)))  # this is the pay for hours of work above forty.
    return pay


pay = compute_pay(h, r)
print("Pay=", pay)
