import numpy as np
import matplotlib.pyplot as plt
import math 
     
pontosX = np.linspace(-np.pi*2, np.pi*2, 512, endpoint=True)
Cosseno,Seno = np.cos(pontosX), np.sin(pontosX)

plt.plot(pontosX,Seno)

plt.show()

t = math.pi / 6
p1 = (pontosX * math.cos(t)) + (Cosseno * math.sin(t))
p2 = -(pontosX * math.sin(t)) + (Cosseno * math.cos(t))

plt.plot(p1, p2, color="purple")
plt.show()