"""Write a while loop that starts at the last character in the string and
works its way backwards to the first character in the string, printing each letter on a
separate line, except backwards"""


def backwards(word):
    index = len(word) - 1
    while index >= 0:
        print(word[index])
        index -= 1


word = input('Please enter a word: ')
backwards(word)
