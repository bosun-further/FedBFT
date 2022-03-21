import numpy as np
import math
from functools import reduce 

# generate random floating point values
from random import seed
from random import randint
from random import random
# seed(10)

def NormalizeData(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))

def divideByNext1zero(data):
    digits_array=[]
    for i in data: 
        count_digits = math.log10(i)+1
        print(count_digits)
        digits_array.append(count_digits)
    return digits_array


def countNumofDigits(data):
    digits_array=[]
    for i in data: 
        count_digits = math.floor(math.log10(i)+1)
        # print(count_digits)
        digits_array.append(count_digits)
    return digits_array


def reduceTo(data):
    digits_array=[]
    # print(data)
    # return digits_array
    for i in  data: 
        print(i)
        count_digits = math.floor(math.log10(i)+1)
        reduceToSingleDigit = i/(math.pow(10,count_digits-1))
        # print(reduceToSingleDigit)
        digits_array.append(reduceToSingleDigit)
    return digits_array


def Average(lst):
    return sum(lst) / len(lst)

seed(10)
fish = []
# generate 2D array
Two2D = []

# generate some integers
lasti=0
def normalization():
    for i in range(10000):
        print(i)
       	# value = randint(0, 9999999999)
       	# print(value)
        # print(i)
       	kl = random()
        adder = random()
        # print(kl)
        if(adder*10 >= 1):
            fish.append(kl * 100 * (math.pow(10, adder*10)))
        else:
            fish.append(kl * 100 * (math.pow(10, adder*100)))
        if((i+1)%10 == 0 and (i+1)!=0):
            global lasti
            Two2D.append(fish[lasti:i])
            lasti = i
        # print(fish)
    # print(fish, type(fish))
    # il = reduceTo(fish)
    # Average(lst)
    # print(il)
    return Two2D


# for _ in range(10):
# Two2D.append(normalization()[:5])
# Two2D.append(normalization()[5:10])
print("Two2D")
normalization()
# print(normalization())
print("len(Two2D)")
print(len(Two2D))
print(Two2D)

reducedTwo2DArray = []
averagedTwo2DArray = []
for i in range(len(Two2D)):
        # for j in range(len(Two2D[i])):
    # if(Two2D[i].len() != 0):
    reducedTwo2DArray.append(reduceTo(Two2D[i]))
        # averagedTwo2DArray.append(Average(Two2D[i]))
                # print(Two2D[i][j])
# print(reducedTwo2DArray)
# print(reducedTwo2DArray)

for i in range(len(reducedTwo2DArray)):
    averagedTwo2DArray.append(Average(reducedTwo2DArray[i]))
print(averagedTwo2DArray)


# x = 0.04
# dist = int(math.log10(abs(x)))

# print(dist)

# sg = reduceTo([312,321,4343,4534,546,567,312312])



# print(Average(sg))

# print(NormalizeData([312,321,4343,4534,546,567,312312]))

