import numpy as np
import math
from functools import reduce 
from random import gauss

import csv

# generate random floating point values
from random import seed
from random import randint
from random import random
# seed(10)
# data = pd.read_csv('metalpipe_FFT1.xl.csv', sep=",", header=None)
# data=data.values

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

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    counter=0
    print("len(averagedTwo2DArray)")
    print(len(averagedTwo2DArray))
    for i in range(len(averagedTwo2DArray)):
	    counter+=1
	    # employee_writer.writerow([counter, counter])
	    employee_writer.writerow([counter, averagedTwo2DArray[i]])
	    # sgvalue = math.fabs(gauss(0, 100))
	    # employee_writer.writerow([counter, sgvalue])



# # data = pd.read_csv('metalpipe_FFT1.xl.csv', sep=",", header=None)
# # data=data.values
# def gaussian(x, height, center, width, offset):
#     return height*np.exp(-(x - center)**2/(2*width**2)) + offset

# def six_gaussians(x, h1, c1, w1, 
# 		h2, c2, w2, 
# 		h3, c3, w3,
# 		h4, c4, w4,
# 		h5, c5, w5,
# 		h6, c6, w6,
# 		offset):
#     return (gaussian(x, h1, c1, w1, offset=0) +
#         gaussian(x, h2, c2, w2, offset=0) +
#         gaussian(x, h3, c3, w3, offset=0) + 
#         gaussian(x, h4, c4, w4, offset=0) + 
#         gaussian(x, h5, c5, w5, offset=0) + 
#         gaussian(x, h6, c6, w6, offset=0) + 
#         offset)

# errfunc6 = lambda p, x, y: (six_gaussians(x, *p) - y)**2

# # guess6= [.22, 360, 65, 
# # 	.22, 834, 65, 
# # 	.39, 1164, 140,
# # 	.59, 1550, 200,
# # 	.3, 1990, 200,
# # 	.3, 2350, 75, 0]

# guess6=[ 19, 1000, 100,
# 	.22, 834, 65, 
# 	.39, 1164, 140,
# 	.59, 1550, 200,
# 	.3, 1990, 200,
# 	.3, 2350, 75, 0
# ]
# optim6, success = optimize.leastsq(errfunc6, guess6[:], args=(data[:,0], data[:,2]))
# # print
# print("Fundamental frequency:  ampl ={0:5.1f}, freq ={1:5.1f} Hz, sigma ={2:5.2f} Hz".format(optim6[0],optim6[1],optim6[2]/2))
# print("First harmonic:  ampl ={0:5.1f}, freq ={1:5.1f} Hz, sigma ={2:5.2f} Hz".format(optim6[3],optim6[4],optim6[5]/2))
# print("Second harmonic:  ampl ={0:5.1f}, freq ={1:5.1f} Hz, sigma ={2:5.2f} Hz".format(optim6[6],optim6[7],optim6[8]/2))
# print("Third harmonic:  ampl ={0:5.1f}, freq ={1:5.1f} Hz, sigma ={2:5.2f} Hz".format(optim6[9],optim6[10],optim6[11]/2))
# print("Fourth harmonic:  ampl ={0:5.1f}, freq ={1:5.1f} Hz, sigma ={2:5.2f} Hz".format(optim6[12],optim6[13],optim6[14]/2))
# print("Fifth harmonic:  ampl ={0:5.1f}, freq ={1:5.1f} Hz, sigma ={2:5.2f} Hz".format(optim6[15],optim6[16],optim6[17]/2))



# plt.scatter(data[:,0], data[:,2], c='pink', label='measurement', marker='.', edgecolors=None)
# plt.plot(data[:,0], six_gaussians(data[:,0], *optim6),
#     c='b', label='fit of 6 Gaussians')
# plt.title("FFT of white noise hitting an open metal tube")
# plt.ylabel("Amplitude")
# plt.xlabel("Frequency (Hz)")
# plt.legend(loc='upper left')
# plt.savefig('result2.png')


# x = 0.04
# dist = int(math.log10(abs(x)))

# print(dist)

# sg = reduceTo([312,321,4343,4534,546,567,312312])



# print(Average(sg))

# print(NormalizeData([312,321,4343,4534,546,567,312312]))

