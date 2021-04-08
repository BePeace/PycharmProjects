""" This script computes factorials of numbers"""

import math

def compute(numbers):
    result = [math.factorial(n) for n in numbers]
    if __name__ == '__main__': #print when executing this file directly but not when importing
        print(result)
    return result

