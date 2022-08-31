# How many times group of three values increased in comparison to the previous one ?
import time
import datetime
import numpy as np

# my_function
def increased_3group(values):
    return (values[3:]>values[:-3]).sum()

def main():
    # parsing input
    values = np.loadtxt('inputs/input_1_1.txt')
    print(increased_3group(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
