#What is the power consupmtion of the submarine improved solution using Counter, zip and splat functions
from math import gamma
import time, datetime
from collections import Counter

def get_gamma_rate(values):
    gamma_rate = ""
    for value in values:
        counter = Counter(value)         
    return 0

def main():
    values = [lines for lines in open('inputs/input_3_1.txt','r').read().splitlines()]
    transposed = list(zip(*values))
    print(get_gamma_rate(transposed))

if __name__ == "__main__":
    st = datetime.datetime.now()
    main()
    # get the end datetime
    et = datetime.datetime.now()
    # get execution time
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    