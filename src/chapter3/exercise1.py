# this program computes the pay for workers according to the hours worked.
x = float(input("Enters hours:"))
y = float(input("Enters rate:"))
z = (x * y)  # this is the pay for hours of work below or equal to 40
q = y * 40
h = (1.5 * (x - 40) * y)  # h is the extra pay for hours worked beyond the 40 hours .
d = (q + h)  # this is the pay for hours of work above forty.
if x <= 40:
    print(z)
elif x > 40:
    print(d)
