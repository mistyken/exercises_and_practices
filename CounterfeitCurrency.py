#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'countCounterfeit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY serialNumber as parameter.
#
# Check currency
# 1. 10 to 12 characters
# 2. first 3 characters are uppercase letters
# 3. next 4 is YYYY year
# 4. next set represent denomation in 10 20 50 100 200 500 1000
# 5. one character uppercase serial letter

def countCounterfeit(serialNumber):
    # Write your code here
    amount = 0
    note_amount = {10,20,50,100,200,500,1000}
    for number in serialNumber:
        try:
            if len(number) < 10 or len(number) > 12:
                continue
            
            first_set = number[0:3]
            if not first_set.isupper() or len(set(first_set)) != 3:
                continue
            
            second_set = number[3:7]
            if int(second_set) < 1900 or int(second_set) > 2019:
                continue
            
            third_set = number[7:]
            if third_set[-1].isupper():
                bill_note = int(third_set[0:-1])
                if bill_note in note_amount:
                    amount += bill_note
            else:
                continue
        except ValueError:
            continue
        
    return amount
    