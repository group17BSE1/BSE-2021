fname = input('Enter a file name: ')
try:
    fhand = open('fname')
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print('File can not be opened: ', fname)
        exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
        print('There are', count, 'subject lines in', fname)
