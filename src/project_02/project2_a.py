"""The program in “project2_a.py” will copy selected lines from “measles.txt” into a
file selected by the user"""
try:
    measles = open("measles.txt", "r")
except FileExistsError:
    exit("File can't be to opened.")
# Prompt for output file name and the year of reference'
file_name = input("Enter the output file name: ")
year = input("Enter a year: ")

try:
    if (year == int(year)) or year == "" or year == "all" or year == "ALL":
        pass
except ValueError:
    print("You have entered a wrong year!")  # an error pops up when the condition above is not satisfied
    exit()

new_file = open(file_name, 'w+')  # This will overwrite the file in case the file name exists already.
count = 0
for line in measles:
    if (line[-5] == year) or (line[-4] == year) or (line[-3] == year) or (line[-1] == year):
        new_file.write(line)  # This is to add data to the new file created.
        count += 1
    elif year == "" or year == "all" or year == "ALL":
        new_file.write(line)  # add content to the new file
        count += 1

if count > 0:
    print("File processing complete you can now check for the file.")
else:
    print("There are no records for the year entered!")
    exit()
