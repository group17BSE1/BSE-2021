"""Encapsulate this code in a function named count, and generalize it so
that it accepts the string and the letter as arguments"""
word = input('Enter a word')
letter = input('Enter a letter')


def count(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)


count(word, letter)
