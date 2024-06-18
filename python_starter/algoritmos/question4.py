#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'smashTheBricks' function below.
#
# The function is expected to return a 2D_LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER bigHits
#  2. INTEGER_ARRAY newtons
#

def smashTheBricks(bigHits, newtons):
    results = []

    for hit in range(1, bigHits + 1):
        result_for_hit = ' '.join(map(str, [newton - hit for newton in newtons]))
        results.append(result_for_hit)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bigHits = int(input().strip())

    newtons_count = int(input().strip())

    newtons = []

    for _ in range(newtons_count):
        newtons_item = int(input().strip())
        newtons.append(newtons_item)

    result = smashTheBricks(bigHits, newtons)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
