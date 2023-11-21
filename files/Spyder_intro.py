# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 22:12:42 2023

@author: ambroise
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import re


# (changer l'adresse du fichier)
folder=r"C:\Users\ambro\Documents\Associations\TutoPython\data"
path2population = os.path.join(folder,"population.csv")
dat = pd.read_csv(path2population,header=1)

# importer le fichier dans la console en faisant "F5"

# afficher un plot interactif en tapant %matplotlib avant l'exécution
def plot_population(pays="FRA"): 
    dat[pays].plot()

# En haut à droite, visualiser les données contenues dans "dat" dans le manager de variables

# dans la console (bas à droite), taper "dat.head()" pour visualiser les premières entrées contenues dans "dat"

# réparer l'erreur en tapant %debug après l'exécution
def ne_marche_pas1():
    x = range(10)
    y = x*2
    plt.plot(x,y)
    
def ne_marche_pas2(a=45,b=23,c=9):
    tab = [a,b,c]
    res = []
    last = 10
    for i in tab:
        res.append(100/(i-4.5*last))
    return res