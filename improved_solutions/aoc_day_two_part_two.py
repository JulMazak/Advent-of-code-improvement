# What is the final coordinations of the submarine with adding the aim?
#using listh comprehension and complex numbers
import time
import datetime


# my_function
def final_depth_with_aim(values):
    values = [(value[0],int(value[1])) for value in values]
    depth = 0+0j
    aim = 0
    for value in values:
        if  (value[0] == "down" ):
            aim += value[1]
        elif (value[0] == "up"):
            aim -= value[1]
        else:
            depth+= complex(value[1],value[1]*aim)

    return int(depth.real * depth.imag)


def main():
    # parsing input
    my_input = open('inputs/input_2_1.txt','r')
    values = [line.split() for line in my_input.read().splitlines()]   
    print(final_depth_with_aim(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
