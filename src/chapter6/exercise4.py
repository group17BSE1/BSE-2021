"""Write an invocation that counts the number of times the letter a occurs in “banana”"""
word = 'banana'
count = 0
for char in word:
    count += 1
print('a', word.count('a', 1, 6))
