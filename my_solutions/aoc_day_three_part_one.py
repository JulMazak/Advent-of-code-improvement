#What is the power consumption of the submarine?
import time
import datetime
#my function
def get_gamma_rate(values):
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(values[0][0])):
        count_zeroes = 0
        for value in values:
            if value[0][i] == "0":
                count_zeroes += 1
        if count_zeroes > len(values)/2:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
        
    return int(gamma_rate, 2)*int(epsilon_rate, 2)

def main():
    values = [lines.split() for lines in open('inputs/input_3_1.txt','r').read().splitlines()]
    print(get_gamma_rate(values))



if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')