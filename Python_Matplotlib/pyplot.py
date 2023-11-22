import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print(matplotlib.__version__)

x=[1, 2, 3, 4, 5]
y=[(lambda k:k*10)(i) for i in x]

plt.plot(x,y)
plt.show()
