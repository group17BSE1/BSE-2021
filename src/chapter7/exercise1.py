"""Write a program to read through a file and print the contents of the file
(line by line) all in upper case."""

fname = input('Enter a file name')  # prompt user for the file name.
fhand = open('fname')
for line in fhand:
    line = line.rstrip()
    print(line.upper())
