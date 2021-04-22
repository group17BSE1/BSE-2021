stock = ('''
25 nickles
25 dimes
25 quarters
0 ones
0 fives
''')


print(">>> =================RESTART=================\n>>>")
print("Welcome to the vending machine change maker program\nChange maker initialized.\nStock contains:")




deposits = ('''
    n - deposit a nickel
    d - deposit a dime
    q - deposit a quarter
    o - deposit a one dollar bill
    f - deposit a five dollar bill
    c - cancel the purchase
''')

input = float(input('enter the purchase price in form of xx.xx $' or ' "q" to quit'))

if input == ('enter the purchase price in form of xx.xx $'):
    print(deposits)
else:
    print(stock)