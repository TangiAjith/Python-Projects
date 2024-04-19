from random import *

words = ['apple', 'banana', 'mango']
word = choice(words)
print(word)
lives = 6
a = []
for i in word:
    a += '_'
print(a)
go = False
while not go:
    guess = input("guess a letter")
    for i in range(len(word)):
        char = word[i]
        if char == guess:
            a[i] = guess
    print(a)
    if guess not in word:
        lives -= 1
        if lives == 0:
            go = True
            print("you lose")
    if '_' not in a:
        go = True
        print("you win")