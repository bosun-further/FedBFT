from random import seed
from random import gauss
import collections
from random import random
import math
import numpy as np
import csv

# seed random number generator
seed(1)
# generate some Gaussian values
def CountFrequency(arr):
    return collections.Counter(arr) 

original = []
with open('freemanson.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    counter=0
    for _ in range(10000):
	    counter+=1
	    sgvalue = gauss(5, 2)
	    if(counter < 100):
	        sgvalue = sgvalue+100
	    if(counter > 400):
	        sgvalue = sgvalue+150
	    original.append(sgvalue) 
	    employee_writer.writerow([counter,  sgvalue])


original.sort()
with open('sorted_freemanson.csv', mode='w') as sorted_file:
    sorted_writer = csv.writer(sorted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    counter=0
    for i in range(len(original)):
	    counter+=1
	    sorted_writer.writerow([counter,  original[i]])

N = np.array(original, int)
freq = CountFrequency(N)
for (key, value) in freq.items():
        print (key, " -> ", value)

with open('int_sorted_freemanson.csv', mode='w') as sorted_file:
    sorted_writer = csv.writer(sorted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    counter=0
    for i in range(len(N)):
	    counter+=1
	    sorted_writer.writerow([counter,  N[i]])


with open('frequency_freemanson.csv', mode='w') as sorted_file:
    sorted_writer = csv.writer(sorted_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for (key, value) in freq.items():
	    sorted_writer.writerow([key,  value])


qatar=np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
print(qatar)
	
    

    