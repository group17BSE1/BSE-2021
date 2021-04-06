# This program prompts the user for score in yhe range 0 to 1 and prints the corresponding grade.
try:
    y = float(input("please enter score in range 0.0...1.0:"))
    if 0 <= y < 0.6:
        print(y, "F")
    elif 0.6 <= y <= 0.69:
        print(y, "D")
    elif 0.7 <= y <= 0.79:
        print(y, "C")
    elif 0.8 <= y <= 0.89:
        print(y, "B")
    elif 0.9 <= y <= 1:
        print(y, "A")
    else:
        print("Bad score")
except:
    print("INVALID ENTRY PLEASE")  # The compiler will print an error message if the user enters wrong data formats
