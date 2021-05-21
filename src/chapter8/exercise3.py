""" Rewrite the guardian code in the above example without two if
statements. Instead, use a compound logical expression using the or logical
operator with a single if statement"""
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if (len(words) > 0) and (words[0] == 'From'):
        print(words[2])
