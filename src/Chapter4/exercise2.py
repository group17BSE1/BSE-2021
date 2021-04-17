c = float(input('Enter investment amount:'))  # c is the initial investment amount
r = float(input('Enter rate per year:'))  # r is the rate per year.
t = float(input('Enter number of years until maturation:'))  # t is the number of years until maturation.
n = float(input('Enter number of times the interest is compounded per year:'))  # n is the number of times the
# interest is compounded per year.


def investment(c, r, n, t):
    p = round(c * (1 + (r / n)) ** (t * n), 2)  # p is the final value of the investment.
    return p


p = investment(c, r, n, t)
print('final investment=', p)
