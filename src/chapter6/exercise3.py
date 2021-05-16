word = input('Enter a word')
letter = input('Enter a letter')


def count(word, letter):
    counter = 0
    for character in word:
        if character == letter:
            counter = counter + 1
    print(counter)


count(word, letter)