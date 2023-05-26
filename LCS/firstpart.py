"""
2-4 Multiplexer Problem
"""
import random

#create random data that is the six bit string list of lists
random_data = [[random.randint(0,1) for i in range(6)] for j in range(100)]
#lets flatten the inner arrays
training_data_X = [''.join([str(i) for i in j]) for j in random_data]
#lets create the y values with respect ot the first 2 digits 00 -> 0 ; 01 -> 1 ; 10 -> 2 ; 11 -> 3 
training_data_y = [str(int(training_data_X[i][0])*2 + int(training_data_X[i][1])) for i in range(len(training_data_X))]

for x,y in zip(training_data_X,training_data_y):
    print(f"X Value -> {x} : y Value -> {y}")
