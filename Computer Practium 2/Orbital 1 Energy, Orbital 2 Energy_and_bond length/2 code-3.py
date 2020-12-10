import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['savefig.dpi'] = 600
matplotlib.rcParams['lines.linewidth'] = 3
plt.rcParams["font.weight"] = "bold"
plt.rcParams["axes.labelweight"] = "bold"
plt.rcParams["axes.linewidth"] = 2.0
plt.rcParams["axes.labelsize"] = 22
filename = 'data.csv'
print('Reading ',filename)
df = pd.read_csv(filename, sep=',')
fig = plt.figure(1, figsize=(8, 6))
ax = plt.subplot(1,1,1)
plt.plot(df['time'],df['func1'], 'b-', label='Orbital 1 Energy') 
plt.plot(df['time'],df['func2'], 'r-', label='Orbital 2 Energy') 
plt.xlabel('bond length',fontsize=22)
plt.ylabel('Total Energy',fontsize=22)
ax.tick_params(labelsize=16, length=6, width=2)
plt.legend(fontsize=20)
plt.savefig("Orbital 1 Energy, Orbital 2 Energy_and_bond length.png")
plt.show()

