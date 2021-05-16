"""he program that prompts the user for the file name so that it prints a funny message when the user
types in the exact file name “na na boo boo”. The program should behave normally
for all other files which exist and don’t exist. Here is a sample execution of the
program:
"""
file_name = input('Enter a file name: ')  # prompt user for file name
try:
    fhand = open('file_name')
except:
    if file_name == 'na na boo boo':  # when user enters the correct file name
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print('File can not be opened: ', file_name)
        exit()
count = 0
for line in 'fhand':
    if line.startswith('Subject:'):
        count = count + 1
        print('There are', count, 'subject lines in', file_name)
