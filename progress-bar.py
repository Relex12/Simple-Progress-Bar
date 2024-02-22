#!/usr/bin/env python3

import sys
import time

def progress_bar(count,total,size=60,sides="[]",full='#',empty='.',prefix=""):
    """
    Displays a progress bar.

    *Prototype*:

    * **count** (*int*) : the current advancement (must be smaller or equal than *total*)
    * **total** (*int*) : the total amount
    * **size** (*int*) : the width of the progress bar, without the brackets and the prefix
    * **sides** (*str*) : the characters to print at the beginning and at the end of the progress bar (must be at least two characters long)
    * **full** (*str*) : the character to print for the done part of the bar (should be one character long)
    * **empty** (*str*) : the character to print for the remaining part of the bar (should be one character long)
    * **prefix** (*str*) : the prefix to print before the progression bar
    """
    x = int(size*count/total)
    sys.stdout.write("\r" + prefix + sides[0] + full*x + empty*(size-x) + sides[1] + ' ' + str(count).rjust(len(str(total)),' ')+"/"+str(total))
    if count==total:
        sys.stdout.write("\n")

if __name__ == '__main__':
    for i in range(1,101):
        progress_bar(count=i,total=100)
        time.sleep(0.01) # place you job here
