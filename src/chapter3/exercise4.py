try:
    # This will execute this block of data if the user puts the right data format
    a = int(input("enter age"))
    if a >= 18:
        print("you can vote")
    elif 0 <= a <= 17:
        print("too young to vote")
    elif a < 0:
        print("you are a time traveller")
except:
    print(" only a digit  input required please")
    # The compiler will print an error message if the user enters wrong data formats
