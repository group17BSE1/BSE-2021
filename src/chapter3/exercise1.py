b = float(input("Enter hours:"))
s = float(input("Enter rate:"))
pay = (b * s)
w = (1.5 * s * b)
if b <= 40:
    print(pay)  # This prints the pay for hours entered from forty and below.

else:
    print(w)  # this prints the extra pay for whoever works for more than 40 hours
