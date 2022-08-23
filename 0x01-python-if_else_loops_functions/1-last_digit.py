#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
modulus = number % 10 if number >= 0 else ((number % 10) * -1)
if modulus > 5:
    print(f"Last digit of {number} is {modulus} and is greater than 5")
elif modulus == 0:
    print(f"Last digit of {number} is {modulus} and is zero")
else:
    print(f"Last digit of {number} is {modulus} and less than 6 and not 0")
