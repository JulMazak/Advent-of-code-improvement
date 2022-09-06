# What is the final coordinations of the submarine?
#improved version , using complex numbers and list comprehension

import time
import datetime
import numpy as np

# my_function
def final_depth(values):
    depth = 0+0j
    DIRECTIONS = {
        'forward':1+0j,
        'up':0-1j,
        'down':0+1j
    }
    complex_values = [(complex_value[0],int(complex_value[1])) for complex_value in values]
    for cv in complex_values:
        depth += cv[1]*DIRECTIONS[cv[0]]

    return (int(depth.real * depth.imag))

def main():
    # parsing input
    my_input = open('inputs/input_2_1.txt','r')
    values = [line.split() for line in my_input.read().splitlines()]
    print(final_depth(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')