#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if abs(number) % 10 > 5:
    if number < 0:
        print("Last digit of %d is %d and is less than 6 and not 0"
              % (number, ((abs(number) % 10) * -1)))
    else:
        print("Last digit of %d is %d and is greater than 5"
              % (number, (abs(number) % 10)))
elif abs(number) % 10 == 0:
    if number < 0:
        print("Last digit of %d is %d and is 0"
              % (number, ((abs(number) % 10) * -1)))
    else:
        print("Last digit of %d is %d and is 0"
              % (number, (abs(number) % 10)))
if (abs(number) % 10 < 6) and (abs(number) % 10 != 0):
    if number < 0:
        print("Last digit of %d is %d and is less than 6 and not 0"
              % (number, ((abs(number) % 10) * -1)))
    else:
        print("Last digit of %d is %d and is less than 6 and not 0"
              % (number, (abs(number) % 10)))
