#/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def dft(x):
    
    X=np.array([])
    wp=np.arange(-10.0,10.0,.01)

    for w in wp:
        s=np.exp(-1j * w * np.arange(x.size))
        X=np.append(X,sum(x*s))

    plt.plot(wp/(2*np.pi),X)
    plt.show()

if __name__='__main__':
    dft(np.array([0,1,2,3]))
