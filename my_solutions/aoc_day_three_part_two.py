#What is the value of life support rating?
import time
import datetime
def get_life_support(values):
    binaries1 = [str(binarie) for binarie in values]
    binaries2 = [str(binarie) for binarie in values]

    for i in range(len(binaries1[0])):
        count_zeroes = 0
        for binarie in binaries1:
            if(binarie[i] == "0"):
                count_zeroes += 1
        if count_zeroes > len(binaries1)/2:
            binaries1 = [str(binarie) for binarie in binaries1 if binarie[i] == "0"]
        else:
            binaries1 = [str(binarie) for binarie in binaries1 if binarie[i] == "1"]
        if(len(binaries1) == 1):
            oxygen =  binaries1[0] 
    for i in range(len(binaries2[0])):
        count_zeroes = 0
        for binarie in binaries2:
            if(binarie[i] == "0"):
                count_zeroes += 1
        if count_zeroes > len(binaries2)/2:
            binaries2= [str(binarie) for binarie in binaries2 if binarie[i] == "1"]
        else:
            binaries2 = [str(binarie) for binarie in binaries2 if binarie[i] == "0"]
        if(len(binaries2) == 1):
            co2 = binaries2[0]
    return int(bin(int(oxygen,2)),2)*int(bin(int(co2,2)),2)

def main():
    values = [lines for lines in open('inputs/input_3_1.txt','r').read().splitlines()]
    print(get_life_support(values))



if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
