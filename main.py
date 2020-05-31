#!/bin/env python3
import random

def diceroll(amount):
    for dice in range(amount):
        print(random.randint(1,6))

diceamount = input('How many dice: ')
diceroll(int(diceamount))