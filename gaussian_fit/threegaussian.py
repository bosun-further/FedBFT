import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

data = np.genfromtxt('employee_file.csv', delimiter=",")
print(data)
def gaussian(x, height, center, width, offset):
    return height*np.exp(-(x - center)**2/(2*width**2)) + offset
def three_gaussians(x, h1, c1, w1, h2, c2, w2, h3, c3, w3, offset):
    return (gaussian(x, h1, c1, w1, offset=0) +
        gaussian(x, h2, c2, w2, offset=0) +
        gaussian(x, h3, c3, w3, offset=0) + offset)

def two_gaussians(x, h1, c1, w1, h2, c2, w2, offset):
    return three_gaussians(x, h1, c1, w1, h2, c2, w2, 0,0,1, offset)


def one_gaussians(x, h1, c1, w1, offset):
    return three_gaussians(x, h1, c1, w1, 0, 0, 1, 0,0,1, offset)

errfunc3 = lambda p, x, y: (three_gaussians(x, *p) - y)**2
errfunc2 = lambda p, x, y: (two_gaussians(x, *p) - y)**2
errfunc1 = lambda p, x, y: (one_gaussians(x, *p) - y)**2

# guess3 = [300, 0.55, 0.01, 0.6, 0.61, 0.01, 1, 0.64, 0.01, 0]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there
# guess2 = [300, 0.55, 0.01, 1, 0.64, 0.91, 0]  # I removed the peak I'm not too sure about
# guess1 = [300, 0.55, 0.01, 0]
guess3 = [300, 0.55, 1000, 0.6, 5000, 0.01, 1000, 300, 0.01, 100]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there
guess2 = [300, 0.55, 0.01, 1, 500, 0.91, 1000]  # I removed the peak I'm not too sure about
guess1 = [1000, 500, 300, 0]

optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(data[:,0], data[:,1]))
# , data[:,1])
optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(data[:,0], data[:,1]))

optim1, success = optimize.leastsq(errfunc1, guess1[:], args=(data[:,0], data[:,1]))
# optim3
print("type")
print(optim3,type(optim3))
print(optim2,type(optim2))
# gmm
plt.plot(data[:,0], data[:,1], lw=1, c='g', label='measurement')
plt.plot(data[:,0], three_gaussians(data[:,0], *optim3),
    lw=3, c='b', label='fit of 3 Gaussians')
plt.plot(data[:,0], two_gaussians(data[:,0], *optim2),
    lw=1, c='m', ls='--', label='fit of 2 Gaussians')
plt.plot(data[:,0], one_gaussians(data[:,0], *optim1),
    lw=1, c='r', ls='--', label='fit of 1 Gaussians')

plt.legend(loc='best')
plt.savefig('result.png')
err3 = np.sqrt(errfunc3(optim3, data[:,0], data[:,1])).sum()
err2 = np.sqrt(errfunc2(optim2, data[:,0], data[:,1])).sum()
print('Residual error when fitting 3 Gaussians: {}\n'
    'Residual error when fitting 2 Gaussians: {}'.format(err3, err2))