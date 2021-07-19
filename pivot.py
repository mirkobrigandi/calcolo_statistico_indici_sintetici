import indici as indice
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from random import *
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\briga\Desktop\Tesi\Dati\Merged.xlsx',sheet_name = "merged",usecols = 'E,F,H,AI')

lista = [1,2,3]
scopo = df[df['SCOPO'].isin(lista)]

pivot = pd.pivot_table(scopo, index = ['SESSO','SCOPO'],
               values = 'FASCIA_ETA',
               columns = 'ATTIVITA',
               aggfunc = [numpy.sum,numpy.mean],
               fill_value = 0,
               margins = True, margins_name = 'Totale')


print (pivot)
pivot.to_excel('pivot.xlsx')






