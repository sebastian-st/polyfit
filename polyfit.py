#!/usr/bin/env python3
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def arrayExport(arr, name):
        f = open(name, "w")
        for items in arr:
                f.write(" ".join([str(a) for a in items]) + "\n")
        f.close()

# Obtain data from interactive mode
fig = plt.figure()
plt.xlim([0, 10])
plt.ylim([0, 10])

X = []
Y = []

def feed(x,y):
	X.append(x)
	Y.append(y)

def onclick(event):
	plt.plot(event.xdata, event.ydata, marker='o', color='tab:blue')
	feed(event.xdata, event.ydata)
	fig.canvas.draw()

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()
plt.close()
arr = [[X[i],Y[i]] for i in range(len(X))]
arrayExport(arr, "output_data.txt")


plt.figure()

# Polynomial fitting function of arbitrary degree
def fit_function(x, *params):
	poly = 0.
	for i, p in enumerate(params):
		poly += p * x**i
	return poly


data = np.genfromtxt("output_data.txt")
X = [x[0] for x in data]
Y = [x[1] for x in data]

# p0 is the initial guess for the fitting coefficients, set the length
# of this to be the order of the polynomial you want to fit. Here I
# have set all the initial guesses to 1., you may have a better idea of
# what values to expect based on your data.
degree = 10
initial_params = np.ones(degree,)

fitted_params, var_matrix = curve_fit(fit_function, X, Y, p0=initial_params)

X_continuous = np.linspace(min(X), max(X), 100)
yfit = [fit_function(x, *tuple(fitted_params)) for x in X_continuous] # I'm sure there is a better
                                                    # way of doing this
plt.plot(X, Y, label='Test data', marker='o', linestyle='')
plt.plot(X_continuous, yfit, label='fitted data')
plt.xlim([0, 10])
plt.ylim([0, 10])

plt.show()

