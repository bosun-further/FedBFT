import numpy as np
import matplotlib.pyplot as mpl
from scipy.optimize import curve_fit
# data =np.loadtxt('employee_file.csv')
data = np.genfromtxt('employee_file.csv', delimiter=",")
my_x=data[:,0]
my_y=data[:,1]

guess3 = [300, 0.55, 1000, 0.6, 5000, 0.01, 1000, 300, 0.01, 100]  # I guess there are 3 peaks, 2 are clear, but between them there seems to be another one, based on the change in slope smoothness there
guess2 = [300, 0.55, 0.01, 1, 500, 0.91, 1000]  # I removed the peak I'm not too sure about
guess1 = [1000, 500, 300, 0]

optim3, success = optimize.leastsq(errfunc3, guess3[:], args=(data[:,0], data[:,1]))
# , data[:,1])
optim2, success = optimize.leastsq(errfunc2, guess2[:], args=(data[:,0], data[:,1]))

optim1, success = optimize.leastsq(errfunc1, guess1[:], args=(data[:,0], data[:,1]))

# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

def gauss(x,mu,sigma,A):
    return A*np.exp(-(x-mu)**2/2/sigma**2)
def trimodal_gauss(x,mu1,sigma1,A1,mu2,sigma2,A2,mu3,sigma3,A3):
    return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)+gauss(x,mu3,sigma3,A3)
    #    """""
    #     Gaussian fitting parameters recognized in each file
    #     """""
first_centroid=(10180.4*2+9)/9
second_centroid=(10180.4*2+(58.6934*1)+7)/9
third_centroid=(10180.4*2+(58.6934*2)+5)/9
centroid=[]
centroid+=(first_centroid,second_centroid,third_centroid)

apparent_resolving_power=1200
sigma=[]
for i in range(len(centroid)):
    sigma.append(centroid[i]/((apparent_resolving_power)*2.355))

height=[1,1,1]

p=[]    
p = np.array([list(t) for t in zip(centroid, sigma, height)]).flatten()
# popt, pcov = curve_fit(trimodal_gauss,my_x,my_y,p0=p) 
# p0=[1,mean,sigma]

# Executing curve_fit on noisy data
popt, pcov = curve_fit(trimodal_gauss,my_x,my_y) 
# popt, pcov = curve_fit(func, x, yn)

print("popt:")
print(popt)
print("pcov:")
print(pcov)

# x = np.linspace(0, 1000, 1000)
x = my_x
fig = mpl.figure()
ax = fig.add_subplot(111)
ax = fig.add_subplot(111)
y = my_y
ax.plot(x, y, c='k', label='Function')

yn = y + 0.1 * np.random.normal(size=len(x))
ax.scatter(x, yn)
fig.savefig('tri.png')


ym = func(x, popt[0], popt[1], popt[2])

# print(ym)
ax.plot(x, ym, c='r', label='Best fit')
ax.scatter(x, my_y)
ax.legend()
fig.savefig('trimodal.png')