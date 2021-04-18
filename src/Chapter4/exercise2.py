""" #this program is to print the final investment after prompting the user for the initial
 investment amount,rate,number of years until maturation and the times the interest is compounded"""
e = input('Enter investment amount:')  # c is the initial investment amount
f = input('Enter rate per year:')  # r is the rate per year.
g = input('Enter number of years until maturation:')  # t is the number of years until maturation.
h = input('Enter number of times the interest is compounded per year:')


def investment(c, r, n, t):
    try:
        c = float(e)
        r = float(f)
        t = float(g)
        n = float(h)
        p = round(c * (1 + (r / n)) ** (t * n), 2)  # p is the final value of the investment.
        return p
    except ValueError:
        print('please enter digits')


p = investment(e, f, g, h)
print('final investment=', p)
