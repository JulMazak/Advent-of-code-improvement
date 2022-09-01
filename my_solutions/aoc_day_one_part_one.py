import time
import datetime
#How many times have value increased in comparison with the previous one ?
# my_function
def increased(values):
    count = 0
    for i in range(1,len(values)):
        if(int(values[i-1])<int(values[i])):
            count+=1
    return count

def main():
    # parsing input
    my_input = open('inputs/input_1_1.txt','r')
    values = my_input.read().splitlines()
    print(increased(values))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()

    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')


