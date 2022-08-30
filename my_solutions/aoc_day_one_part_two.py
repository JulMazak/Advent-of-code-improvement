# How many times group of three values increased in comparison to the previous one ?

#parsing
my_input = open('inputs/input_1_1.txt','r')
values = my_input.read().splitlines()
count = 0

for i in range (len(values) - 3 ):
    if ((int(values[i]) + int(values[i+1]) + int (values[i+2])) < (int(values[i+1])+int(values[i+2])+int(values[i+3]))):
        count+=1
print(count)