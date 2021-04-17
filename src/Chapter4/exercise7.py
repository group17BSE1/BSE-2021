def compute_grade(t):
    if 0.0 <= t <= 1.0:
        if t >= 0.9:
            return 'A'
        if t >= 0.8:
            return 'B'
        if t >= 0.7:
            return 'C'
        if t >= 0.6:
            return 'D'
        else:
            return 'F'
    return 'Bad score'  # this is the error message printed whenever score out of range is input.


t = input('enter the score:')  # this prompts the user to input the score.
try:
    t = float(t)  # this converts the user input to afloat value
except ValueError:
    print('Big error,enter digits only!')  # this is the error printed when non-numeric input is entered
    quit()  # this terminates the execution of the program completely

grade = compute_grade(t)
print(grade)
