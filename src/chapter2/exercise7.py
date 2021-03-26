c = float(input("please enter an amount to make change: "))
print('your change is...')
print(c//20, "twenties")
c = (c%20)
print(c//10, "ten")
c = c%10
print(c//5, "fives")
c = c%5
print(c//1, "ones")
c = c%1
print(c//0.25, "quarters")
c = c%0.25
print(c//0.1, "dimes")
c = c%0.1
print(c//0.05, "nickels")
c = c%0.05
print(c//0.01, "pennies")
