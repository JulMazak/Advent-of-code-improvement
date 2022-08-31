import time
import datetime
import numpy as np 

#How many times have value increased in comparison with the previous one ?
# my_function
def increased(values):
    return(values[1:]>values[:-1]).sum()

def main():
    # parsing input
    values = np.loadtxt('inputs/input_1_1.txt')
    print(increased(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')


