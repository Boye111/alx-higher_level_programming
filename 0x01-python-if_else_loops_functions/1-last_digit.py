#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    ls_dt = number % 10
else:
    ls_dt = ((number * -1) % 10) * -1

if ls_dt > 5:
    print(f'Last digit of {number} is {ls_dt} and is greater than 5')
elif ls_dt == 0:
    print(f'Last digit of {number} is {ls_dt} and is 0')
elif ls_dt < 6 and ls_dt != 0:
    print(f'Last digit of {number} is {ls_dt} and is less than 6 and not 0')
