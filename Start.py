# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 10:39:22 2025

@author: natha
"""
import pandas as pd
import numpy as np

# importation of datasets
from sklearn import datasets

# Iris datasets loading

# iris = datasets.load_iris()

data = pd.read_excel(r'Iris.xls', sheet_name='Data')     
len(data)

# To have a look to null cells in the EDA
data.isna().sum()

# EDA Exploring Data Analysis
variables = ['Petal_width', 'Petal_length', 'Sepal_width', 'Sepal_length']

# delete row of null cells
cleandf = data.dropna(subset=variables)

df = cleandf

# Correct the name of species and cut none need column
df = df.replace("Verginica", 'Virginica', regex=True)
df = df.drop('Species_No', axis=1)

# Have global descriprion of data
df.describe()

# Have description of data based on they species name and turn it vertical
dtable = df.groupby(['Species_name']).describe()
dtable = dtable.transpose()

#Univariate visual EDA on ' Iris numerical variables

import matplotlib
import matplotlib.pyplot as plot
import seaborn as sns

# df[variables].hist()

# Perform bivariate visual EDA ising Sepal caracteristics
# sns.scatterplot(x=df["Sepal_length"], y=df["Sepal_width"], hue=df["Species_name"])
# sns.jointplot(x=df["Sepal_length"], y=df["Sepal_width"], hue=df["Species_name"])

# plot.boxplot(df[variables])

# sns.boxplot(x=df["Species_name"], y=df["Sepal_length"])
sns.pairplot(df, hue='Species_name', palette='OrRd')



















