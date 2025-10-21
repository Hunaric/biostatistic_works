# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:07:20 2025

@author: natha
"""

# Load libraries
import pandas as pd
from scipy import stats
# import os
# os.chdir(r'C:\Users\natha\Desktop\BioStat\05 - Libraries for biostatistics hypothesis tests in Python')
# print(os.getcwd())


# Load the diabets datasets
brut_data = pd.read_csv('Dataset of Diabetes.csv')

# Select subject with confirm diabets
all_data = brut_data[brut_data['CLASS']=='Y']

# define the separate datasets for Male-M and Female-F
data1 = all_data[all_data['Gender']=='F']
data2 = all_data[all_data['Gender']=='M']

# select the high density lipoprotein (HDL)
HDLf = data1['HDL']
HDLm = data2['HDL']

import matplotlib.pyplot as plt

# create a list of label of x-axis
labels = ['HDLf', 'HDLm']

# create a list of heighs for the bars
heights = [HDLf.mean(), HDLm.mean()]

# create a bar plot 
plt.bar(labels, heights)

# Add label and title
plt.xlabel('Gender')
plt.ylabel('HDL')
plt.title('Mean HDL level by Gender')

# Display the plot

plt.show()
















