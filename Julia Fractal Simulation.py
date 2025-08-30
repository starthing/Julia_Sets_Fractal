import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
res = 500
x = np.linspace(-1.5, 1.5, res)
y = np.linspace(-1.5, 1.5, res)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y

def julia(c, max_iter=100):
    z = Z.copy()
    img = np.zeros(Z.shape)
    for i in range(max_iter):
        z = z**2 + c
        img[np.abs(z) < 100] += 1
    return img

def animate(i):
    ax.clear()
    c = np.cos(i/20)*0.7885 + 1j*np.sin(i/20)*0.7885
    img = julia(c)
    ax.imshow(img, cmap='twilight_shifted', extent=(-1.5, 1.5, -1.5, 1.5))
    ax.axis('off')

ani = animation.FuncAnimation(fig, animate, frames=120, interval=10)
plt.show()
