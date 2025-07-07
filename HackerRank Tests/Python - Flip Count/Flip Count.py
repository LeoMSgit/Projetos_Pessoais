#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'theFinalProblem' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING target as parameter.
#

def theFinalProblem(target):
    flip_count = 0
    current_state = '0'
    for bit in target:
        if bit != current_state:
            flip_count += 1
            current_state = '1' if current_state == '0' else '0'
    return flip_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    target = input()

    result = theFinalProblem(target)

    fptr.write(str(result) + '\n')

    fptr.close()
