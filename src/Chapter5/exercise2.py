count = 0
total = 0
avg = 0
largest = None
smallest = None
keepgoing = True
while keepgoing:  # this will iterate along the code block as long as the condition is true
    number = 'Enter a number '
    line = input(number)
    try:  # this helps to check the cod block and if there ae no errors the code is executed
        line = float(line)
        count = count + 1
        total = total + line
        avg = total / count
        if smallest is None or line < smallest:
            smallest = line
        if largest is None or line > largest:
            largest = line
    except ValueError:  # this helps to check the cod block and if there ae no errors the code is executed
        if line == 'Done' or line == 'done':
            break  # #break this will terminate the while loop and execute other codes outside the loop
        else:
            print('Invalid Input')
            continue  # this rejects all the remaining statements in the current iteration of the loop and moves the
            # control back to the top of the loop.
print('maximum = ', largest, 'minimum = ', smallest)
