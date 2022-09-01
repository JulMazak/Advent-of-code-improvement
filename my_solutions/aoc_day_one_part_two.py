# How many times group of three values increased in comparison to the previous one ?
import time
import datetime

# my_function
def increased_3group(values):
    count = 0
    for i in range (len(values) - 3 ):
        if ((int(values[i]) + int(values[i+1]) + int (values[i+2])) < (int(values[i+1])+int(values[i+2])+int(values[i+3]))):
            count+=1
    return count

def main():
    # parsing input
    my_input = open('inputs/input_1_1.txt','r')
    values = my_input.read().splitlines()
    print(increased_3group(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
