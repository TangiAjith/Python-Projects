from random import *
from math import *

a = int(input("enter lower bound"))
b = int(input("enter upper bound"))
c = randint(a, b)
d = round(log(b - a + 1, 2))
print("you have only", d, "chances to guess")
count = 0
while count < d:
    count += 1
    guess = int(input("guess a number:"))
    if guess == d:
        print("you guessed the correct number in ", count, "tries")
        break
    elif guess < d:
        print("your number is too small")
    elif guess > d:
        print("your number is too high")
if count >= d:
    print("the number is:", c)
    print("better luck next time")