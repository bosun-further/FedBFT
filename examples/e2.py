import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl

from scipy import optimize
data = np.genfromtxt('frequency_freemanson.csv', delimiter=",")
# Let's create a function to model and create data
def func(x, a, x0, sigma):
	return a*np.exp(-(x-x0)**2/(2*sigma**2))

# Generating clean data
# x = np.linspace(0, 10, 100)
print("len(data[:,0])")
print(len(data[:,0]))
print( data[:,0][len(data[:,0])-1])
x = np.linspace(data[:,0][0], data[:,0][len(data[:,0])-1], len(data[:,0]))
# x = data[:,0]
# len(data[:,0])
# guess3 = [300, 0.55, 1000, 0.6, 5000, 0.01, 1000, 300, 0.01, 100]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there
# guess2 = [300, 0.55, 0.01, 1, 500, 0.91, 1000]  # I removed the peak I'm not too sure about
# guess1 = [1000, 500, 300, 0]
# optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(data[:,0], data[:,1]))
# # , data[:,1])
# optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(data[:,0], data[:,1]))
# optim1, success = optimize.leastsq(errfunc1, guess1[:], args=(data[:,0], data[:,1]))



y = func(x, 50, 40, 20)

# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))+20
my_y = data[:,1]
# Plot out the current state of the data and model
fig = mpl.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, c='k', label='Function')
# ax.scatter(x, yn)

ax.scatter(x, my_y)
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, my_y)

#popt returns the best fit values for parameters of the given model (func)
print (popt)

ym = func(x, popt[0], popt[1], popt[2])
ax.plot(x, ym, c='r', label='Best fit')
ax.legend()
fig.savefig('model_fit.png')

