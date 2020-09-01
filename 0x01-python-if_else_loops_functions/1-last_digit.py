#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "and is greater than 5"
b = "and is 0"
c = "and is less than 6 and not 0"
print("Last digit of", end=" ")
if number % 10 > 5:
    print("{} is {} {}".format(number, number % 10, a))
elif number % 10 == 0:
    print("{} is {} {}".format(number, number % 10, b))
elif number < 0:
    print("{} is {} {}".format(number, ((number * -1) % 10) * -1, c))
else:
    print("{} is {} {}".format(number, number % 10, c))
