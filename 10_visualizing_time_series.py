# -*- coding: utf-8 -*-
"""10 Visualizing time series (2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OP9mUDWciya5KbXPhjA_MGU-e8HYasoB

##Visualizing time series
"""

import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from pylab import rcParams

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
rcParams['figure.figsize'] = 5, 4



"""### The simplest time series plot"""

from google.colab import files
uploaded = files.upload()
df = pd.read_csv('Superstore-Sales.csv', index_col='Order Date', encoding='cp1252', parse_dates=True)
df.head()

df['Order Quantity'].plot() # cannot see any insight with this because there are so many date

df2 = df.sample(n=100, random_state=1, axis=0)

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()

df2 = df.sample(n=100, random_state=25, axis=0)

plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Superstore Sales')

df2['Order Quantity'].plot()