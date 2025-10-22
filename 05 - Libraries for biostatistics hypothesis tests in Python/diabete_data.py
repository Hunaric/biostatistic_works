# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 11:07:20 2025

@author: natha
"""

# Load libraries
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Uncomment this line to access the dataset file
# import os
# os.chdir(r'C:\Users\natha\Desktop\BioStat\05 - Libraries for biostatistics hypothesis tests in Python')
# print(os.getcwd())


# Load the diabets datasets
brut_data = pd.read_csv('Dataset of Diabetes.csv')

# Select subject with confirm diabets
all_data = brut_data[brut_data['CLASS']=='Y']

# define the separate datasets for Male-M and Female-F
# data1 = all_data[(all_data['Gender']=='F') | (all_data['Gender']=='f')]
# data2 = all_data[(all_data['Gender']=='M') | (all_data['Gender']=='m')]
data1 = all_data[all_data['Gender']=='F']
data2 = all_data[all_data['Gender']=='M']


"""
# HDL section

# select the high density lipoprotein (HDL)
HDLf = data1['HDL']
HDLm = data2['HDL']


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

#We use t_test  which is a t-test for independent samples for this dataset because males and females are independant of each other


# LDL section
# perform t-test for the HDL between gender
t_statistic, p_value = stats.ttest_ind(HDLf, HDLm)

# print result
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")
"""


# t_test for the Low Density Lipoprotein between gender in diabetics
LDLf = data1['LDL']
LDLm = data2['LDL']

# List of label for teh x-axis
labels = ['LDLf', 'LDLm']

heights = [LDLf.mean(), LDLm.mean()]

# create a bar plot
plt.bar(labels, heights)

# label and title
plt.xlabel('Gender')
plt.ylabel('LDL')
plt.title('Mean LDL levels by gender')

# Display the plot
plt.show()

# perform t_test
t_statistic, p_value = stats.ttest_ind(LDLf, LDLm)

# print result
print(f"t-statistic: {t_statistic}")
print(f"p-value: {p_value}")









