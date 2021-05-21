"""Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user
enters “done”. Write the program to store the numbers the user enters in a list and use
the max() and min() functions to compute the maximum and minimum numbers
after the loop completes.
"""
num_list = []  # create an empty list for storing the numbers from the user.
while True:
    input_number = input('Enter a number: ')  # prompt for user input.
    if input_number == 'done'.lower():
        break

    try:
        number = float(input_number)
    except ValueError:  # error pops up when something other than a number.
        print('Invalid input,please enter a number!')
        continue

    num_list.append(number)  # add each number input to the list that was created above

if num_list:
    print(num_list)
    print('Maximum: ', max(num_list) or None)
    print('Minimum: ', min(num_list) or None)
