# this program reads an integer from input representing someone's age and prints the votabillity of the user.
try:
    a = int(input("enter age"))
    if a >= 18:#caters for age from 18 and above.
        print("you can vote")
    elif 0 <= a <= 17:
        print("too young to vote")
    elif a < 0:
        print("you are a time traveller")
except:
    print(" only a digit  input required please")
    # The compiler will print an error message if the user enters wrong data formats