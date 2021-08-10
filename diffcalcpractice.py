import numpy as np
from math import sin
import matplotlib.pyplot as plt
 
dx = .01
def f(x):
    return x**2*sin(x) + 2
function_y = [f(x) for x in np.arange(0,20,dx)] 
function_x = [x for x in np.arange(0,20,dx)]
 
function_deriv = np.gradient(function_y,dx)

plt.plot(function_x, function_deriv, linestyle='--', label="h=" + str(dx))
plt.title("Convergence to Derivative by varying h")
plt.legend()
plt.show()
