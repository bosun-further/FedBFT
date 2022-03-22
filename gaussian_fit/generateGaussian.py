from random import seed
from random import gauss

from random import random
import math
import numpy as np
import csv

# seed random number generator
seed(1)
# generate some Gaussian values

with open('freemanson.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    counter=0
    for _ in range(1000):
	    counter+=1
	    sgvalue = gauss(1, 10)
	    employee_writer.writerow([counter, sgvalue+random()])


qatar=np.random.choice(np.arange(1, 7), p=[0.1, 0.05, 0.05, 0.2, 0.4, 0.2])
print(qatar)
	
    

    