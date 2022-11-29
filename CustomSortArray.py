#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'moves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

# Determine min number of move to make all left element of 
# an array event and all right element of an array odd

def moves(arr):
    # Write your code here
    left_index = 0
    right_index = len(arr) - 1
    moves = 0
    while left_index < right_index:
        print("comparing {} {}".format(arr[left_index], arr[right_index]))
        if arr[left_index] % 2 == 0 and arr[right_index] % 2 != 0:
            left_index += 1
            right_index -= 1
        elif arr[left_index] % 2 == 0 and arr[right_index] % 2 == 0:
            left_index += 1
        elif arr[left_index] % 2 != 0 and arr[right_index] % 2 != 0:
            right_index -= 1
        else:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            moves += 1
            left_index += 1
            right_index -= 1
    return moves