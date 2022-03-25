import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
import matplotlib.pyplot as plt
# 无法调用curvefit，对于多个Gaussian

from scipy import optimize
data = np.genfromtxt('frequency_freemanson.csv', delimiter=",")
# Let's create a function to model and create data
def gufunc(x, a, x0, sigma):
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

def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset
def three_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, offset):
    return (gaussian(x, h1, c1, w1, offset=0) +
        gaussian(x, h2, c2, w2, offset=0) +
        gaussian(x, h3, c3, w3, offset=0) + offset)

def two_gaussians(x, h1, c1, w1, h2, c2, w2, offset):
    return three_gaussians(x, h1, c1, w1, h2, c2, w2, 0,0,1, offset)


def one_gaussians(x, h1, c1, w1, offset):
     return gaussian(x, h1, c1, w1, offset=0)

def gufunc(x, a, x0, sigma):
     return a*np.exp(-(x-x0)**2/(2*sigma**2))

def gauss(x,mu,sigma,A):
    return A*np.exp(-(x-mu)**2/2/sigma**2)
def trimodal_gauss(x,mu1,sigma1,A1,mu2,sigma2,A2,mu3,sigma3,A3):
    return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)+gauss(x,mu3,sigma3,A3)
    #    """""

# [1894.87079845  129.16999379    8.87005261]
y = gufunc(x, 50, 40, 20)
# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))+20
my_y = data[:,1]
# Plot out the current state of the data and model
fig = mpl.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, c='k', label='Function from core Gaussian Function')
ax.scatter(x, my_y)
# Executing curve_fit on noisy data
popt, pcov = curve_fit(gufunc, x, my_y)
#popt returns the best fit values for parameters of the given model (gufunc)
print (popt)

ym = gufunc(x, popt[0], popt[1], popt[2])
ax.plot(x, ym, c='r', label='Best fit')
ax.legend()
fig.savefig('model_fit.png')


# gmm
# data[:,0]


errfunc3 = lambda p, x, y: (three_gaussians(x, *p) - y)**2
errfunc2 = lambda p, x, y: (two_gaussians(x, *p) - y)**2
errfunc1 = lambda p, x, y: (one_gaussians(x, *p) - y)**2

guess3 = [1, 50, 40, 20, 100, 1500, 20, 100, 160, 1]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there
guess2 = [1, 50, 40, 20, 100, 1500, 20]  # I removed the peak I'm not too sure about
# guess1 = [1, 1000, 130, 0]
guess1 =  [1,50, 40, 20]
optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(x, data[:,1]))
optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(x, data[:,1]), maxfev=100000)
optim1, success = optimize.leastsq(errfunc1, guess1[:], args=(x, data[:,1]))

plt.plot(x, data[:,1], lw=1, c='g', label='measurement')
plt.plot(data[:,0], three_gaussians(data[:,0], *optim3),
    lw=3, c='g', label='fit of 3 Gaussians')
plt.plot(x, two_gaussians(x, *optim2),
    lw=1, c='g', ls=':', label='fit of 2 Gaussians')
plt.plot(x, one_gaussians(x, *optim1),
    lw=1, c='b', ls='--', label='fit of 1 Gaussians')


plt.legend(loc='best')
plt.savefig('result.png')