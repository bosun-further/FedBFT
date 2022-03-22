import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
import math
from functools import reduce 
from random import gauss

import csv

# generate random floating point values
from random import seed
from random import randint
from random import random

# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))




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

# with open('employee_file.csv', mode='w') as employee_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     counter=0
#     print("len(averagedTwo2DArray)")
#     print(len(averagedTwo2DArray))
#     for i in range(len(averagedTwo2DArray)):
# 	    counter+=1
# 	    # employee_writer.writerow([counter, counter])
# 	    employee_writer.writerow([counter, averagedTwo2DArray[i]])

# Generating clean data
x = np.linspace(0, 1000, 1000)
y1 = []
for i in range(len(averagedTwo2DArray)):
    # counter+=1
    # employee_writer.writerow([counter, counter])
    y1=averagedTwo2DArray[i]
	    # employee_writer.writerow([counter, averagedTwo2DArray[i]])
# y1 = func(x[np.where(x <= 10)], 1, 3, 1)
# y1 = func(x, 1, 3, 1)
# y2 = func(x[np.where((x>10) & (x<20))], -2, 15, 0.5)
# y3 = func(x[np.where((x>=20) & (x<30))], -5, 10, 9)
# y4 = func(x[np.where((x>=30) & (x<40))], 50, 10, 9)
# y5 = func(x[np.where((x>=40))], -10, 100, 90)
# y2 = func(x[np.where(x > 10)], -2, 15, 0.5)

# Stack arrays in sequence horizontally (column wise).
# y = np.hstack([y1, y2, y3, y4, y5])
y = np.hstack(averagedTwo2DArray)
# y = np.hstack([y1, y2])

# Adding noise to the data
yn = y + 0.1 * np.random.normal(size=len(x))
# yn = y

# Plot out the current state of the data and model
fig = mpl.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, c='k', label='Function')
ax.scatter(x, yn)
fig.savefig('model_and_noise_multiple.png')

# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)

#popt returns the best fit values for parameters of the given model (func)
#popt: Optimal values for the parameters so that the SSR (sum of the squared residuals) of [f(xdata, *popt) - ydata] is minimized
print(popt)

# The estimated CO-VARIANCE of popt. 
# The diagonals provide the VARIANCE of the parameter estimate. 
# To compute one SDE on the parameters use perr = np.sqrt(np.diag(pcov)).
# SDE: standard deviation errors 
print(pcov)

ym = func(x, popt[0], popt[1], popt[2])
# print(ym)
ax.plot(x, ym, c='r', label='Best fit')
ax.legend()
fig.savefig('model_fit_multiple.png')