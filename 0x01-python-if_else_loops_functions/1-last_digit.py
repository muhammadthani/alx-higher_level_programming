#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = abs(number) % 10
if number < 0:
    mod = -mod
print(f"Last mod of {number:d} is {mod:d} and is ", end="")
if mod == 0:
    print("0")
elif mod > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
