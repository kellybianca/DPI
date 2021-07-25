from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 30)
y = np.linspace(-10, 10, 20)

x, y = np.meshgrid(x, y)

a = 3 
b = 7 

x1 = (x**2) / (a**2)
y1 = (y**2) / (b**2)
z = (x1 + y1)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(x,y,z, rstride=1, cstride=1,
                cmap='winter', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
