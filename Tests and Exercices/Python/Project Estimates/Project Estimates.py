#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts the following parameters:
#  1. INTEGER_ARRAY projectCosts
#  2. INTEGER target
#

def countPairs(projectCosts, target):
    # Create a set to store the project costs for O(1) lookups
    costs_set = set(projectCosts)
    count = 0
    
    # Iterate over each cost in the original list
    for cost in projectCosts:
        # Check if the cost + target exists in the set
        if (cost + target) in costs_set:
            count += 1
        # Check if the cost - target exists in the set
        if (cost - target) in costs_set:
            count += 1
    
    # Each pair (a, b) is counted twice (once for a and once for b), so divide by 2
    return count // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    projectCosts_count = int(input().strip())

    projectCosts = []

    for _ in range(projectCosts_count):
        projectCosts_item = int(input().strip())
        projectCosts.append(projectCosts_item)

    target = int(input().strip())

    result = countPairs(projectCosts, target)

    fptr.write(str(result) + '\n')

    fptr.close()
