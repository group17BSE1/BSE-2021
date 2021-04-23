
stock = ('''
25 nickles
25 dimes
25 quarters
0 ones
0 fives
''')
def start_start():
    print(">>> =================RESTART=================\n>>>")
    print("Welcome to the vending machine change maker program\nChange maker initialized.\nStock contains:")
    print(stock)

start_start()







deposits = ('''
    enter:
    n to deposit a nickel
    d to deposit a dime
    q to deposit a quarter
    o to deposit a one dollar bill
    f to deposit a five dollar bill
    c to cancel the purchase
''')

def enter_price():
    print('please enter your pay')
    print(deposits)



try:
    price = float(input('Enter price in form of xx.xx or q to quit'))
    enter_price()
except ValueError:
    start_start()




c = float(input("please enter an amount to make change: "))
print('payment due is : ')
print(c//5, "fives")
c = c%5
print(c//1, "ones")
c = c%1
print(c//0.25, "quarters")
c = c%0.25
print(c//0.1, "dimes")
c = c%0.1
print(c//0.05, "nickels")





