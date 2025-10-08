# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 12:19:04 2025

@author: natha
"""

# Importation des bibliothèques necessaire pour ce projet
import pandas as pd
from sklearn import datasets
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Lecture des donnees grace a Pandas
data = pd.read_csv(r'Dataset of Diabetes .csv')

"""
Ce dataset est constitué de :
    - Index du patient
    - Genre du patient
    - Age du patient
    - Ratio de creatinine (CR)
    - Index de masse corporelle (BMI)
    - Urée du patient
    - Son Cholesterol (Chol)
    - Son profil lipidique a jeun total (LDL et VLDL)
    - Son Triglycérides (TG)
    - Sa plus haute densité lipoproteine (HDL)
    - Hemoglobine (HbA1c) Taux de sucre dans le sang sur les 3 derniers mois
"""

# Pour voir le nombre total d'echantillon dans notre dataset
len(data)

data.isna().sum()

# On change le nom de notre variable pour plus de clarté dans le code. On le nomera df (diminutif de dataframe)
df = data

# Suppression des colonnes qui n'auront pas un effet sur notre avancé: nom et index des patients
df = df.drop(['ID', 'No_Pation'], axis=1)

# On retire les patient dont la class est Predict-Diabetic pour avoir que des valeurs sures avec lesquelles travailler
df = df[df["CLASS"].str.contains("P") == False]

len(df)

# Groupons les valeurs par genre et transposons pour un affichage beaucoup plus propre
dtable1 = df.groupby(['Gender']).describe()
dtable1 = dtable1.transpose()

# Correction de l'erreur de frappe avec f a la place de F pour le genre 
df = df.replace('f', 'F', regex=True)
dtable1 = df.groupby(['Gender']).describe()
dtable1 = dtable1.transpose()

# Grouper les valeurs par classe diabetique ou non et transposons
dtable2 = df.groupby(['CLASS']).describe()
dtable2 = dtable2.transpose()

# Correction de l affichage a cause de l espace entre le N et le Y
df['CLASS'] = df['CLASS'].str.strip()
dtable2 = df.groupby(['CLASS']).describe()
dtable2 = dtable2.transpose()

# Groupons les valeur en fonctions de deux variables, le genre et la classe
table_final = df.groupby(['Gender', 'CLASS']).describe()
table_final = table_final.transpose()


















