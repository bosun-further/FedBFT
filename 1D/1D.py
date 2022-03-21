import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl

# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))

# Generating clean data
x = np.linspace(0, 200, 200)

y1 = func(x[np.where(x <= 10)], 1, 3, 1)
# y1 = func(x, 1, 3, 1)
y2 = func(x[np.where((x>10) & (x<20))], -2, 15, 0.5)
y3 = func(x[np.where((x>=20) & (x<30))], -5, 10, 9)
y4 = func(x[np.where((x>=30) & (x<40))], 50, 10, 9)
y5 = func(x[np.where((x>=40))], -10, 100, 90)
# y2 = func(x[np.where(x > 10)], -2, 15, 0.5)

# Stack arrays in sequence horizontally (column wise).
y = np.hstack([y1, y2, y3, y4, y5])
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