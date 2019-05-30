#!/usr/bin/env python
# coding: utf-8

# In[68]:


# libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import os

# Data
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Morph.csv")
#df

# y-axis in bold
#rc('font', weight='bold')

# Values of each group
bars1 = df.plate_phill
bars2 = df.plate_pacif
bars3 = df.plate_maria
bars4 = df.plate_carol
 
# The position of the bars on the x-axis
profiles = df.profile
 
# Names of group and bar width
names = ["profile1", "profile2", "profile3", "profile4", "profile5", 
         "profile6", "profile7","profile8", "profile9", "profile10",
         "profile11", "profile12", "profile13", "profile14", "profile15",
         "profile16", "profile17", "profile18", "profile19", "profile20",
         "profile21", "profile22", "profile23", "profile24", "profile25"]
barWidth = 1
 
# Create bars
ax = plt.subplot(111)
plt.bar(profiles, bars1, color='#dbd0e6', edgecolor='white', width=barWidth, label='Philippine Plate')
plt.bar(profiles, bars2, bottom=(bars1), color='#a0d8ef', edgecolor='white', width=barWidth, 
        label='Pacific Plate')
plt.bar(profiles, bars3, bottom=(bars1 + bars2), color='#eebbcb', edgecolor='white', width=barWidth,
       label='Mariana Plate')
plt.bar(profiles, bars4, bottom=(bars1 + bars2 + bars3), color='#c1d8ac', edgecolor='white', width=barWidth,
       label='Caroline Plate')
 
# Custom X axis
plt.xticks(profiles, names, fontweight='normal', fontsize=7, rotation=30)
 
# Show graphic
plt.legend()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10), shadow=True, 
          markerscale=2, ncol=4, fontsize=6, title=False)
plt.title('Mariana Trench: Stacked barplots for the distribution \nof the bathymetric observations across tectonic plates', 
          fontsize=10, fontfamily='sans-serif')
plt.show()


# In[ ]:





# In[ ]:




