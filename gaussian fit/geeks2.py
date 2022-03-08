import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as mpl
import matplotlib.pyplot as plt

# Let's create a function to model and create data
def func(x, a, x0, sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))
  
# Generating clean data
x = np.linspace(0, 10, 100)
y = func(x, 1, 5, 2)
  
# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))
  
# Plot out the current state of the data and model
fig = mpl.figure()
ax = fig.add_subplot(111)
ax.plot(x, y, c='k', label='Function')
ax.scatter(x, yn)
  
# Executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)
  
#popt returns the best fit values for parameters of the given model (func)
print (popt)

  
ym = func(x, popt[0], popt[1], popt[2])
ax.plot(x, ym, c='r', label='Best fit')
ax.legend()
fig.savefig('model_fit.png')





# e^(a * b)
e_exp_a_x_b = [426.0938, 259.2896, 166.8042, 80.9248]
# a * b
a_x_b = np.log(e_exp_a_x_b)
# b
b = np.array([50,300,600,1000])

def fun(x,a_slope,b_intercept):
    return a_slope * x + b_intercept

x_data = b
y_data = a_x_b
fig2 = mpl.figure(figsize=(6, 4))
ax2 = fig2.add_subplot(111)
ax2.plot(x_data, fun(x_data, popt[0], popt[1]),
         label='Fitted function')
ax2.legend(loc='best')
fig2.savefig('model_fit2.png')