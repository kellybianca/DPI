import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.stats import multivariate_normal

def gaussian(N=2, M=1000, m=0, sigma=1):
    mean = np.zeros(N) + m  
    cov = np.eye(N) * sigma  

    data = np.random.multivariate_normal(mean, cov, M)
    Gaussian = multivariate_normal(mean=mean, cov=cov)
    return data, Gaussian

data, Gaussian = gaussian(N=2, M=1000, sigma=0.1)
x = np.linspace(-1,1,1000)
y = np.linspace(-1,1,1000)
x, y = np.meshgrid(x, y)

d = np.dstack([x,y])
z = Gaussian.pdf(d).reshape(1000,1000)

fig = plt.figure(figsize=(6,4))
ax = plt.axes(projection="3d")
ax.plot_surface(x, y, z, cmap='winter')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()