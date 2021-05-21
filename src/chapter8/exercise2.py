"""
We can cause an IndexError by passing this program a line which
starts with "From" but containing nothing else. This passes the first test, the
length of the line is > 0. The second test checks if the line starts with
"From" and the program proceeds to try to print words[2] which does not exist.
We can guard against this case by adding an "or" test to check that the line
contains a 3rd item
"""

fhand = open('measles.short.txt', 'r')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 or len(words) < 3:
        continue
    if words[0] != 'From':
        continue
    print(words[2])
