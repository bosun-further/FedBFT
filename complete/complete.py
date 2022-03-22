from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt


# Now, let's create an initial guess for our parameters. 
# This guess starts with peaks at x=0 and x=1,000 with amplitude 60,000 and e-folding widths of 80. 
# Then, 
# we add candidate peaks at x=60, 140, 220, ... with amplitude 46,000 and width of 25:
data = np.loadtxt('edata_s.csv', delimiter=',')
x = data[:,0]
y = data[:,1]

plt.plot(x,y)
plt.show()

def func(x, *params):
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        y = y + amp * np.exp( -((x - ctr)/wid)**2)
    return y

guess = [0, 60000, 80, 1000, 60000, 80]
for i in range(12):
    guess += [60+80*i, 46000, 25]   

popt, pcov = curve_fit(func, x, y, p0=guess)
print(popt)
fit = func(x, *popt)

plt.plot(x, y)
plt.plot(x, fit , 'r-')
plt.show()