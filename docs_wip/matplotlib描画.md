```python
import matplotlib.pyplot as plt
import numpy as np


class MyPlot:
    @classmethod
    def init(cls):
        plt.gca().axis('off')          # 枠線や目盛りを消す
        plt.gca().set_aspect('equal')  # 縦横比を揃える
    @classmethod
    def show(cls):
        plt.show()
    @classmethod
    def point(cls, x, y, size=10):
        plt.scatter(x, y, s=size)
    @classmethod
    def line(cls, x, y, lw=1):
        plt.plot(x, y, lw=lw)
    @classmethod
    def ellipse(cls, xc, yc, a, b, angle=0, lw=1):
        theta = np.linspace(0, 2*np.pi, 100)
        x0 = a*np.cos(theta)
        y0 = b*np.sin(theta)
        x = xc + x0*np.cos(angle) - y0*np.sin(angle)
        y = yc + x0*np.sin(angle) + y0*np.cos(angle)
        cls.line(x, y, lw=lw)
    @classmethod
    def circle(cls, xc, yc, r, lw=1):
        cls.ellipse(xc, yc, r, r, lw=lw)

MyPlot.init()
MyPlot.ellipse(1, 2, 4, 6, np.pi/6)
plt.show()



```