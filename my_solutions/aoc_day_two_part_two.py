# What is the final coordinations of the submarine with adding the aim?
import time
import datetime
import numpy as np

# my_function
def final_depth_with_aim(values):
    horizontal = 0
    vertical = 0
    aim = 0
    for value in values:
        v = x = value.split()
        if (v[0] == "forward"):
            horizontal += int(v[1])
            vertical += int(v[1])*aim
        if  (v[0] == "down" ):
            aim += int(v[1])
        if (v[0] == "up"):
            aim -= int(v[1])
    return horizontal*vertical


def main():
    # parsing input
    my_input = open('inputs/input_2_1.txt','r')
    values = my_input.read().splitlines()
    print(final_depth_with_aim(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
