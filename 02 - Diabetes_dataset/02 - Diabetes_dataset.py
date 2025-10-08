# -*- coding: utf-8 -*-
"""
Analyse exploratoire d’un dataset de patients pour l’étude du diabète.

Ce script lit un dataset CSV contenant des informations médicales de patients et effectue :
    - le nettoyage des données
    - le regroupement par genre et classe
    - l’analyse descriptive des variables
    - la préparation pour une analyse du profil lipidique et du taux de sucre

Colonnes du dataset :
    - ID : identifiant unique du patient
    - No_Patient : numéro du patient
    - Gender : genre du patient (M/F)
    - Age : âge du patient
    - Creatinine_ratio : ratio de créatinine
    - BMI : index de masse corporelle
    - Urea : taux d’urée
    - Chol : cholestérol total
    - LDL_VLDL : profil lipidique à jeun total
    - TG : triglycérides
    - HDL : haute densité lipoprotéique
    - HbA1c : hémoglobine glyquée, indicateur du taux de sucre moyen sur 3 mois
    - CLASS : classification diabétique ou non

Auteur : Nathan
Date : 08/10/2025
"""

# Importation des bibliothèques necessaire pour ce projet
import pandas as pd
from sklearn import datasets
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

# Lecture des donnees grace a Pandas
data = pd.read_csv(r'Dataset of Diabetes .csv')

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

# Dans la suite du projet, nous allons suivre le profil de lipide des patients (LDL, HDL et TG) ainsi que leur taux ed sucre dans le sang

# On stocke ces differentes valeurs dans une variable
variables = ['TG', 'LDL', 'HDL', 'HbA1c']

# Utilisation de sns.displot pour analyser les differentes variables

"""
Figure pour le HbA1c des patients diabetiques 
- L'absisse x prend en compte la variation HbA1c
- kde signifie Kernel Density Estimate et permet de tracer une courbe representant la densite de probabilité au lieu d afficher un histogramme
- Changer kind="kde" de sns.displot() par multiple="stack" pour avoir des histogrammes
On pourra changer les variables pour voir son comportement vis a vis des differents patients
"""
# sns.displot(data=df[variables], x='HbA1c', hue=df['CLASS'], multiple="stack")
# sns.displot(data=df[variables], x='TG', hue=df['CLASS'], multiple="stack")
# sns.displot(data=df[variables], x='LDL', hue=df['CLASS'], multiple="stack")
# sns.displot(data=df[variables], x='HDL', hue=df['CLASS'], multiple="stack")

# Pour une visualisation bivariée, on peut utiliser scatter plot de seaborn
# sns.scatterplot(x=df["BMI"],y=df["HbA1c"],hue=df["CLASS"])

# Visualisation avec jointplot pour la separation des points de dispersion par class

# sns.jointplot(x=df["BMI"],y=df["HbA1c"],hue=df["CLASS"])


"""
De toutes ces observations, on retient que la plupart des témoins presentent un taux faible de BMI et de HbA1c pendant que les patients diabétiques ont un taux nettement plus élevé
Dans cette suite, nous allons afficher des graphes en se basant principalement sur le HbA1c, jusqu'a nouvel ordre. Pour aller plus loin, nous allons aussi les considerer par genre.
"""
# Creation des bougies de HbA1c vs CLASS avec boxplot
sns.boxplot(x="Gender", y="HbA1c", hue="CLASS", data=df)
plt.title("Répartition de l'HbA1c par genre et par classe")
plt.show()









