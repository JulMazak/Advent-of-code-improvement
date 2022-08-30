#How many times have value increased in comparison with the previous one ?

# parsing input
my_input = open('inputs/input_1_1.txt','r')
values = my_input.read().splitlines()

count = 0

# actual code
for i in range(1,len(values)):
    if(int(values[i-1])<int(values[i])):
        count+=1
print(count)