
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   codice di calcolo di diversi indici sintetici per analisi statistica di scelte modali di trasporto
#
#   Mirko Brigandi: briga.mirko@gmail.com
#   
#   Luglio 2021
#--------------------------------------------------------------------------------------------------------------------------------------------------------------


#Import delle diverse librerie utili e dei diversi codici creati come supporto
import indici as indice
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from random import *

#Definizione titoli colonne file excel
nomi = numpy.array(['Uomo (1) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Uomo (1) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Donna (2) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Uomo (1)– fascia di età (4) over 65  – attivita (10) pensionato – scopo (6) cure e visite mediche',
					'Donna (2) – fascia di età (4) over 65  – attivita (10) pensionato – scopo (6) cure e visite mediche',
					'Donna (2) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (9) casalinga – scopo (4, 5 e 9) acquisti e commissioni, accompagnamento, visite a parenti ed amici',
					'Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (9) casalinga – scopo (4, 5 e 9) acquisti e commissioni, accompagnamento, visite a parenti ed amici',
					'Uomo (1) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (8) studente – scopo (3) studio',
					'Uomo (1) – fascia di età (1) tra gli 11 ed i 19 anni – attivita (8) studente – scopo (3) studio',
					'Donna (2) – fascia di età (1) tra gli 11 ed i 19 anni – attivita (8) studente – scopo (3) studio',
					'Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (8) studente – scopo (3) studio',
					'Uomo (1) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Uomo (1) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di lavoro',
					'Donna (2) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di studio',
					'Valori MAX','Valori MIN'], dtype='str')


#Definizione array indici sintetici
#Array - Gini Index
m=numpy.ones(18)
#Array - Herfindahl Index
n=numpy.ones(18)
#Array - Theil Index
o=numpy.ones(18)
#Array - Dalton Index
p=numpy.ones(18)
#Array - Atkinson Index
q=numpy.ones(18)
#Array - Shannon Index
r=numpy.ones(18)

#Scelta random dell'ε
eps = (randint(1,10))/10
while eps == 1:
	eps = (randint(1,10))/10
print('Il valore di ε risulta essere: ')
print(eps)

#Vado ad estrapolare dal foglio di lavoro excel solo le informazioni di mio interesse

#sex = codice per il sesso dell'intervistato (1 = uomo; 2 = donna)
sex = pd.read_excel(r'C:\Users\briga\Desktop\Tesi\Dati\Merged.xlsx', sheet_name = "merged", usecols = "E", header = 0, nrows = 117860)

#age = fascia di età dell'intervistato (1 = da 11 a 19; 2 = da 20 a 49; 3 = da 50 a 64; 4 = over 65)
age = pd.read_excel(r'C:\Users\briga\Desktop\Tesi\Dati\Merged.xlsx', sheet_name = "merged", usecols = "F", header = 0, nrows = 117860)

#scopo = motivo dello spostamento dell'intervistato
scopo = pd.read_excel(r'C:\Users\briga\Desktop\Tesi\Dati\Merged.xlsx', sheet_name = "merged", usecols = "H", header = 0, nrows = 117860)

#mezzo = mezzo di trasporto usato dall'intervistato
mezzo = pd.read_excel(r'C:\Users\briga\Desktop\Tesi\Dati\Merged.xlsx', sheet_name = "merged", usecols = "P", header = 0, nrows = 117860)

#attivita = occupazione professionale dell'intervistato
attivita = pd.read_excel(r'C:\Users\briga\Desktop\Tesi\Dati\Merged.xlsx', sheet_name = "merged", usecols = "AI", header = 0, nrows = 117860)




#Definizione array caratteristiche profili
sex1 = numpy.array(sex, dtype='f')


age1=numpy.array(age, dtype='f')


scopo1=numpy.array(scopo, dtype='f')


mezzo1=numpy.array(mezzo, dtype='f')


attivita1=numpy.array(attivita, dtype='f')


#DEFINIZIONE DEI PROFILI E CALCOLO DEI DIVERSI INDICI SINTETICI PER CIASCUN PROFILO

print('Il profilo 1 risulta essere: ')
print('Uomo (1) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro ')
profilo1 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==2) & (attivita1[i]==3) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo1=profilo1 + 1

print('Il numero totale di intervistati ricadenti nel profilo 1 risultano essere: ')
print(profilo1)

index = 0
approvato = numpy.ones(profilo1)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==2) & (attivita1[j]==3) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato[index]=mezzo1[j]
		index = index + 1

m[0] = indice.gini(approvato)
n[0] = indice.hhi(approvato)
o[0] = indice.theil(approvato)
p[0] = indice.dalton(approvato,eps)
q[0] = indice.atkinson(approvato,eps)
r[0] = indice.shannon(approvato)

print('Il profilo 2 risulta essere: ')
print('Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro ')
profilo2 = 0
for i in range(0,117859):
	if ((sex1[i]==2) & (age1[i]==2) & (attivita1[i]==3) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo2=profilo2 + 1

print('Il numero totale di intervistati ricadenti nel profilo 2 risultano essere: ')
print(profilo2)

index1 = 0
approvato1 = numpy.ones(profilo2)
for j in range(0,117859):
	if ((sex1[j]==2) & (age1[j]==2) & (attivita1[j]==3) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato1[index1]=mezzo1[j]
		index1 = index1 + 1

m[1] = indice.gini(approvato1)
n[1] = indice.hhi(approvato1)
o[1] = indice.theil(approvato1)
p[1] = indice.dalton(approvato1,eps)
q[1] = indice.atkinson(approvato1,eps)
r[1] = indice.shannon(approvato1)


print('Il profilo 3 risulta essere: ')
print('Uomo (1) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro ')
profilo3 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==3) & (attivita1[i]==3) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo3=profilo3 + 1

print('Il numero totale di intervistati ricadenti nel profilo 2 risultano essere: ')
print(profilo3)

index2 = 0
approvato2 = numpy.ones(profilo3)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==3) & (attivita1[j]==3) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato2[index2]=mezzo1[j]
		index2 = index2 + 1

m[2] = indice.gini(approvato2)
n[2] = indice.hhi(approvato2)
o[2] = indice.theil(approvato2)
p[2] = indice.dalton(approvato2,eps)
q[2] = indice.atkinson(approvato2,eps)
r[2] = indice.shannon(approvato2)


print('Il profilo 4 risulta essere: ')
print('Donna (2) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (3) impiegato – scopo (1 e 2) recarsi al lavoro e motivi di lavoro ')
profilo4 = 0
for i in range(0,117859):
	if ((sex1[i]==2) & (age1[i]==3) & (attivita1[i]==3) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo4=profilo4 + 1

print('Il numero totale di intervistati ricadenti nel profilo 4 risultano essere: ')
print(profilo4)

index3 = 0
approvato3 = numpy.ones(profilo4)
for j in range(0,117859):
	if ((sex1[j]==2) & (age1[j]==3) & (attivita1[j]==3) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato3[index3]=mezzo1[j]
		index3 = index3 + 1

m[3] = indice.gini(approvato3)
n[3] = indice.hhi(approvato3)
o[3] = indice.theil(approvato3)
p[3] = indice.dalton(approvato3,eps)
q[3] = indice.atkinson(approvato3,eps)
r[3] = indice.shannon(approvato3)


print('Il profilo 5 risulta essere: ')
print('Uomo (1)– fascia di età (4) over 65  – attivita (10) pensionato – scopo (6) cure e visite mediche ')
profilo5 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==4) & (attivita1[i]==10) & (scopo1[i]==6)):
		profilo5=profilo5 + 1

print('Il numero totale di intervistati ricadenti nel profilo 5 risultano essere: ')
print(profilo5)

index4 = 0
approvato4 = numpy.ones(profilo5)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==4) & (attivita1[j]==10) & (scopo1[j]==6)):
		approvato4[index4]=mezzo1[j]
		index4 = index4 + 1

m[4] = indice.gini(approvato4)
n[4] = indice.hhi(approvato4)
o[4] = indice.theil(approvato4)
p[4] = indice.dalton(approvato4,eps)
q[4] = indice.atkinson(approvato4,eps)
r[4] = indice.shannon(approvato4)



print('Il profilo 6 risulta essere: ')
print('Donna (2) – fascia di età (4) over 65  – attivita (10) pensionato – scopo (6) cure e visite mediche ')
profilo6 = 0
for i in range(0,117859):
    if ((sex1[i]==2) & (age1[i]==4) & (attivita1[i]==10) & (scopo1[i]==6)):
        profilo6=profilo6 + 1

print('Il numero totale di intervistati ricadenti nel profilo 6 risultano essere: ')
print(profilo6)

index5 = 0
approvato5 = numpy.ones(profilo6)
for j in range(0,117859):
    if ((sex1[j]==2) & (age1[j]==4) & (attivita1[j]==10) & (scopo1[j]==6)):
        approvato5[index5]=mezzo1[j]
        index5 = index5 + 1

m[5] = indice.gini(approvato5)
n[5] = indice.hhi(approvato5)
o[5] = indice.theil(approvato5)
p[5] = indice.dalton(approvato5,eps)
q[5] = indice.atkinson(approvato5,eps)
r[5] = indice.shannon(approvato5)




print('Il profilo 7 risulta essere: ')
print('Donna (2) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (9) casalinga – scopo (4, 5 e 9) acquisti e commissioni, accompagnamento, visite a parenti ed amici')
profilo7 = 0
for i in range(0,117859):
    if ((sex1[i]==2) & (age1[i]==3) & (attivita1[i]==9) & ((scopo1[i]==4) or (scopo1[i]==5) or (scopo1[i]==9))):
        profilo7=profilo7 + 1

print('Il numero totale di intervistati ricadenti nel profilo 7 risultano essere: ')
print(profilo7)

index6 = 0
approvato6 = numpy.ones(profilo7)
for j in range(0,117859):
    if ((sex1[j]==2) & (age1[j]==3) & (attivita1[j]==9) & ((scopo1[j]==4) or (scopo1[j]==5) or (scopo1[j]==9))):
        approvato6[index6]=mezzo1[j]
        index6 = index6 + 1

m[6] = indice.gini(approvato6)
n[6] = indice.hhi(approvato6)
o[6] = indice.theil(approvato6)
p[6] = indice.dalton(approvato6,eps)
q[6] = indice.atkinson(approvato6,eps)
r[6] = indice.shannon(approvato6)


print('Il profilo 8 risulta essere: ')
print('Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (9) casalinga – scopo (4, 5 e 9) acquisti e commissioni, accompagnamento, visite a parenti ed amici')
profilo8 = 0
for i in range(0,117859):
    if ((sex1[i]==2) & (age1[i]==2) & (attivita1[i]==9) & ((scopo1[i]==4) or (scopo1[i]==5) or (scopo1[i]==9))):
        profilo8=profilo8 + 1

print('Il numero totale di intervistati ricadenti nel profilo 8 risultano essere: ')
print(profilo8)

index7 = 0
approvato7 = numpy.ones(profilo8)
for j in range(0,117859):
    if ((sex1[j]==2) & (age1[j]==2) & (attivita1[j]==9) & ((scopo1[j]==4) or (scopo1[j]==5) or (scopo1[j]==9))):
        approvato7[index7]=mezzo1[j]
        index7 = index7 + 1

m[7] = indice.gini(approvato7)
n[7] = indice.hhi(approvato7)
o[7] = indice.theil(approvato7)
p[7] = indice.dalton(approvato7,eps)
q[7] = indice.atkinson(approvato7,eps)
r[7] = indice.shannon(approvato7)



print('Il profilo 9 risulta essere: ')
print('Uomo (1) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (8) studente – scopo (3) studio ')
profilo9 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==2) & (attivita1[i]==8) & (scopo1[i]==3)):
		profilo9=profilo9 + 1

print('Il numero totale di intervistati ricadenti nel profilo 9 risultano essere: ')
print(profilo9)

index8 = 0
approvato8 = numpy.ones(profilo9)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==2) & (attivita1[j]==8) & (scopo1[j]==3)):
		approvato8[index8]=mezzo1[j]
		index8 = index8 + 1

m[8] = indice.gini(approvato8)
n[8] = indice.hhi(approvato8)
o[8] = indice.theil(approvato8)
p[8] = indice.dalton(approvato8,eps)
q[8] = indice.atkinson(approvato8,eps)
r[8] = indice.shannon(approvato8)


print('Il profilo 10 risulta essere: ')
print('Uomo (1) – fascia di età (1) tra gli 11 ed i 19 anni – attivita (8) studente – scopo (3) studio ')
profilo10 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==1) & (attivita1[i]==8) & (scopo1[i]==3)):
		profilo10=profilo10 + 1

print('Il numero totale di intervistati ricadenti nel profilo 10 risultano essere: ')
print(profilo10)

index9 = 0
approvato9 = numpy.ones(profilo10)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==1) & (attivita1[j]==8) & (scopo1[j]==3)):
		approvato9[index9]=mezzo1[j]
		index9 = index9 + 1

m[9] = indice.gini(approvato9)
n[9] = indice.hhi(approvato9)
o[9] = indice.theil(approvato9)
p[9] = indice.dalton(approvato9,eps)
q[9] = indice.atkinson(approvato9,eps)
r[9] = indice.shannon(approvato9)



print('Il profilo 11 risulta essere: ')
print('Donna (2) – fascia di età (1) tra gli 11 ed i 19 anni – attivita (8) studente – scopo (3) studio ')
profilo11 = 0
for i in range(0,117859):
	if ((sex1[i]==2) & (age1[i]==1) & (attivita1[i]==8) & (scopo1[i]==3)):
		profilo11=profilo11 + 1

print('Il numero totale di intervistati ricadenti nel profilo 11 risultano essere: ')
print(profilo11)

index10 = 0
approvato10 = numpy.ones(profilo11)
for j in range(0,117859):
	if ((sex1[j]==2) & (age1[j]==1) & (attivita1[j]==8) & (scopo1[j]==3)):
		approvato10[index10]=mezzo1[j]
		index10 = index10 + 1

m[10] = indice.gini(approvato10)
n[10] = indice.hhi(approvato10)
o[10] = indice.theil(approvato10)
p[10] = indice.dalton(approvato10,eps)
q[10] = indice.atkinson(approvato10,eps)
r[10] = indice.shannon(approvato10)



print('Il profilo 12 risulta essere: ')
print('Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (8) studente – scopo (3) studio ')
profilo12 = 0
for i in range(0,117859):
	if ((sex1[i]==2) & (age1[i]==2) & (attivita1[i]==8) & (scopo1[i]==3)):
		profilo12=profilo12 + 1

print('Il numero totale di intervistati ricadenti nel profilo 12 risultano essere: ')
print(profilo12)

index11 = 0
approvato11 = numpy.ones(profilo12)
for j in range(0,117859):
	if ((sex1[j]==2) & (age1[j]==2) & (attivita1[j]==8) & (scopo1[j]==3)):
		approvato11[index11]=mezzo1[j]
		index11 = index11 + 1

m[11] = indice.gini(approvato11)
n[11] = indice.hhi(approvato11)
o[11] = indice.theil(approvato11)
p[11] = indice.dalton(approvato11,eps)
q[11] = indice.atkinson(approvato11,eps)
r[11] = indice.shannon(approvato11)



print('Il profilo 13 risulta essere: ')
print('Uomo (1) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di lavoro')
profilo13 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==2) & (attivita1[i]==5) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo13=profilo13 + 1

print('Il numero totale di intervistati ricadenti nel profilo 13 risultano essere: ')
print(profilo13)

index12 = 0
approvato12 = numpy.ones(profilo13)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==2) & (attivita1[j]==5) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato12[index12]=mezzo1[j]
		index12 = index12 + 1

m[12] = indice.gini(approvato12)
n[12] = indice.hhi(approvato12)
o[12] = indice.theil(approvato12)
p[12] = indice.dalton(approvato12,eps)
q[12] = indice.atkinson(approvato12,eps)
r[12] = indice.shannon(approvato12)



print('Il profilo 14 risulta essere: ')
print('Donna (2) – fascia di età (2) tra gli 20 ed i 49 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di lavoro')
profilo14 = 0
for i in range(0,117859):
	if ((sex1[i]==2) & (age1[i]==2) & (attivita1[i]==5) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo14=profilo14 + 1

print('Il numero totale di intervistati ricadenti nel profilo 14 risultano essere: ')
print(profilo14)

index13 = 0
approvato13 = numpy.ones(profilo14)
for j in range(0,117859):
	if ((sex1[j]==2) & (age1[j]==2) & (attivita1[j]==5) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato13[index13]=mezzo1[j]
		index13 = index13 + 1

m[13] = indice.gini(approvato13)
n[13] = indice.hhi(approvato13)
o[13] = indice.theil(approvato13)
p[13] = indice.dalton(approvato13,eps)
q[13] = indice.atkinson(approvato13,eps)
r[13] = indice.shannon(approvato13)



print('Il profilo 15 risulta essere: ')
print('Uomo (1) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di lavoro')
profilo15 = 0
for i in range(0,117859):
	if ((sex1[i]==1) & (age1[i]==3) & (attivita1[i]==5) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo15=profilo15 + 1

print('Il numero totale di intervistati ricadenti nel profilo 15 risultano essere: ')
print(profilo15)

index14 = 0
approvato14 = numpy.ones(profilo15)
for j in range(0,117859):
	if ((sex1[j]==1) & (age1[j]==3) & (attivita1[j]==5) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato14[index14]=mezzo1[j]
		index14 = index14 + 1

m[14] = indice.gini(approvato14)
n[14] = indice.hhi(approvato14)
o[14] = indice.theil(approvato14)
p[14] = indice.dalton(approvato14,eps)
q[14] = indice.atkinson(approvato14,eps)
r[14] = indice.shannon(approvato14)



print('Il profilo 16 risulta essere: ')
print('Donna (2) – fascia di età (3) tra gli 50 ed i 64 anni – attivita (5) insegnante – scopo (1 e 2) recarsi al lavoro e motivi di studio ')
profilo16 = 0
for i in range(0,117859):
	if ((sex1[i]==2) & (age1[i]==3) & (attivita1[i]==5) & ((scopo1[i]==1) or (scopo1[i]==2))):
		profilo16=profilo16 + 1

print('Il numero totale di intervistati ricadenti nel profilo 16 risultano essere: ')
print(profilo16)

index15 = 0
approvato15 = numpy.ones(profilo16)
for j in range(0,117859):
	if ((sex1[j]==2) & (age1[j]==3) & (attivita1[j]==5) & ((scopo1[j]==1) or (scopo1[j]==2))):
		approvato15[index15]=mezzo1[j]
		index15 = index15 + 1

m[15] = indice.gini(approvato15)
n[15] = indice.hhi(approvato15)
o[15] = indice.theil(approvato15)
p[15] = indice.dalton(approvato15,eps)
q[15] = indice.atkinson(approvato15,eps)
r[15] = indice.shannon(approvato15)


m[16] = 0
n[16] = 0
o[16] = 0
p[16] = 0
q[16] = 0
r[16] = 0
m[17] = 0
n[17] = 0
o[17] = 0
p[17] = 0
q[17] = 0
r[17] = 0


#Calcolo valori massimi tra gli indici sintetici
valore_max_gini = max(m)
m[16] = valore_max_gini
valore_max_hhi = max(n)
n[16] = valore_max_hhi
valore_max_theil = max(o)
o[16] = valore_max_theil
valore_max_dalton = max(p)
p[16] = valore_max_dalton
valore_max_atkinson = max(q)
q[16] = valore_max_atkinson
valore_max_shannon = max(r)
r[16] = valore_max_shannon


m[17] = 1
n[17] = 1
o[17] = 1
p[17] = 1
q[17] = 1
r[17] = 1


#Calcolo valori minimi tra gli indici sintetici
valore_min_gini = min(m)
m[17] = valore_min_gini
valore_min_hhi = min(n)
n[17] = valore_min_hhi
valore_min_theil = min(o)
o[17] = valore_min_theil
valore_min_dalton = min(p)
p[17] = valore_min_dalton
valore_min_atkinson = min(q)
q[17] = valore_min_atkinson
valore_min_shannon = min(r)
r[17] = valore_min_shannon





print('I diversi valori dei Gini Index risultano essere: ')
print(m)
print('I diversi valori dei Herfindahl Index risultano essere: ')
print(n)
print('I diversi valori dei Theil Index risultano essere: ')
print(o)
print('I diversi valori dei Dalton Index per ε uguale a ' + str(eps) + ' risultano essere: ')
print(p)
print('I diversi valori dei Atkinson Index per ε uguale a ' + str(eps) + ' risultano essere: ')
print(q)
print('I diversi valori degli Shannon Index risultano essere: ')
print(r)



#Creazione file excel con risultati analisi indici

columns = ["Profilo1", "Profilo2", "Profilo3","Profilo4","Profilo5","Profilo6","Profilo7","Profilo8","Profilo9","Profilo10","Profilo11","Profilo12","Profilo13","Profilo14","Profilo15","Profilo16","MAX","MIN"]
rows = ["Descrizione","Gini Index","Herfindahl Index","Theil Index","Dalton Index","Atkinson Index","Shannon Index"]
dati_indici = numpy.array([nomi,m,n,o,p,q,r])
dataset_indici = pd.DataFrame(data=dati_indici, index=rows, columns=columns)
print(dataset_indici)
dataset_indici.to_excel('Valori_indici_profili.xlsx')



#Creazione grafici di confronto tra i diversi indici

plt.plot(m, n, marker = "o", color = 'blue',linestyle="")
plt.title("Gini VS Herfindahl -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Gini Index") 
plt.ylabel("Herfindahl Index")
#plt.show()
plt.savefig("imagine1.png")
plt.clf()


plt.plot(m, o, marker = "o", color = 'red',linestyle="")
plt.title("Gini VS Theil -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Gini Index") 
plt.ylabel("Theil Index")
#plt.show()
plt.savefig("imagine2.png")
plt.clf()

plt.plot(m, p, marker = "o", color = 'green',linestyle="")
plt.title("Gini VS Dalton -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Gini Index") 
plt.ylabel("Dalton Index")
#plt.show()
plt.savefig("imagine3.png")
plt.clf()

plt.plot(m, q, marker = "o", color = 'orange',linestyle="")
plt.title("Gini VS Atkinson -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Gini Index") 
plt.ylabel("Atkinson Index")
#plt.show()
plt.savefig("imagine4.png")
plt.clf()

plt.plot(n, o, marker = "o", color = 'cyan',linestyle="")
plt.title("Herfindahl VS Theil -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Herfindahl Index") 
plt.ylabel("Theil Index")
#plt.show()
plt.savefig("imagine5.png")
plt.clf()

plt.plot(n, p, marker = "o", color = 'magenta',linestyle="")
plt.title("Herfindahl VS Dalton -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Herfindahl Index") 
plt.ylabel("Dalton Index")
#plt.show()
plt.savefig("imagine6.png")
plt.clf()

plt.plot(n, q, marker = "o", color = 'yellow',linestyle="")
plt.title("Herfindahl VS Atkinson -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Herfindahl Index") 
plt.ylabel("Atkinson Index")
#plt.show()
plt.savefig("imagine7.png")
plt.clf()

plt.plot(o, p, marker = "o", color = 'black',linestyle="")
plt.title("Theil VS Dalton -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Theil Index") 
plt.ylabel("Dalton Index")
#plt.show()
plt.savefig("imagine8.png")
plt.clf()

plt.plot(o, q, marker = "o", color = 'grey',linestyle="")
plt.title("Theil VS Atkinson -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Theil Index") 
plt.ylabel("Atkinson Index")
#plt.show()
plt.savefig("imagine9.png")
plt.clf()

plt.plot(p, q, marker = "o", color = 'purple',linestyle="")
plt.title("Dalton VS Atkinson -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Dalton Index") 
plt.ylabel("Atkinson Index")
#plt.show()
plt.savefig("imagine10.png")
plt.clf()

plt.plot(r, m, marker = "o", color = 'blue',linestyle="")
plt.title("Shannon VS Gini -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Shannon Index") 
plt.ylabel("Gini Index")
#plt.show()
plt.savefig("imagine11.png")
plt.clf()

plt.plot(r, n, marker = "o", color = 'purple',linestyle="")
plt.title("Shannon VS Herfindahl -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Shannon Index") 
plt.ylabel("Herfindahl Index")
#plt.show()
plt.savefig("imagine12.png")
plt.clf()

plt.plot(r, o, marker = "o", color = 'blue',linestyle="")
plt.title("Shannon VS Theil -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Shannon Index") 
plt.ylabel("Theil Index")
#plt.show()
plt.savefig("imagine13.png")
plt.clf()

plt.plot(r, p, marker = "o", color = 'purple',linestyle="")
plt.title("Shannon VS Dalton -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Shannon Index") 
plt.ylabel("Dalton Index")
#plt.show()
plt.savefig("imagine14.png")
plt.clf()

plt.plot(r, q, marker = "o", color = 'blue',linestyle="")
plt.title("Shannon VS Atkinson -- Mezzo")
plt.grid()
plt.xlim(0,1)
plt.ylim(0,1)
plt.xlabel("Shannon Index") 
plt.ylabel("Atkinson Index")
#plt.show()
plt.savefig("imagine15.png")
plt.clf()

#Creazione Istogrammi rappresentanti il numero di intervistati per ciascun profilo

#Istogramma 1

x = numpy.array(['Profilo1','Profilo2','Profilo3','Profilo4'])
y = numpy.array([profilo1,profilo2,profilo3,profilo4])

plt.bar(x,y,label='Istogramma', color = 'aquamarine', )

plt.xlabel('Profili',size= 'x-large')
plt.ylabel('Totali',size='x-large')

plt.title('Istogramma 1')
#plt.show()
plt.savefig("istogram1.png")
plt.clf()


#Istogramma 2

x1 = numpy.array(['Profilo5','Profilo6','Profilo7','Profilo8'])
y1 = numpy.array([profilo5,profilo6,profilo7,profilo8])

plt.bar(x1,y1,label='Istogramma', color = 'coral')

plt.xlabel('Profili',size= 'x-large')
plt.ylabel('Totali',size='x-large')

plt.title('Istogramma 2')
#plt.show()
plt.savefig("istogram2.png")
plt.clf()


#Istogramma 3

x2 = numpy.array(['Profilo9','Profilo10','Profilo11','Profilo12'])
y2 = numpy.array([profilo9,profilo10,profilo11,profilo12])

plt.bar(x2,y2,label='Istogramma', color = 'aquamarine')

plt.xlabel('Profili',size= 'x-large')
plt.ylabel('Totali',size='x-large')

plt.title('Istogramma 3')
#plt.show()
plt.savefig("istogram3.png")
plt.clf()


#Istogramma 4

x3 = numpy.array(['Profilo13','Profilo14','Profilo15','Profilo16'])
y3 = numpy.array([profilo13,profilo14,profilo15,profilo16])

plt.bar(x3,y3,label='Istogramma', color = 'coral')

plt.xlabel('Profili',size= 'x-large')
plt.ylabel('Totali',size='x-large')

plt.title('Istogramma 4')
#plt.show()
plt.savefig("istogram4.png")
plt.clf()

