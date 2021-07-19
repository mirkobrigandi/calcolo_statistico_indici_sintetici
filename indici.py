#Import delle diverse librerie utili
import numpy as np
from numpy import log as ln

#DEFINIZIONE FORMULE INDICI SINTETICI


#FORMULA GINI INDEX
def gini(array):
    """Calculate the Gini coefficient of a numpy array."""
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Gini coefficient:
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array)))


#FORMULA Herfindahl Index
def hhi(array):
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    #Media
    media=np.mean(array)

    # HHI coefficient:

    return((1/n)*(1+(n*(np.sum((array-media)**2))/(np.sum(array**2)))))



#FORMULA Theil Index
def theil(array):
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    #Media
    media=np.mean(array)


    # Theil coefficient:
    return((np.sum((array/media)*ln(array/media)))/n)



#FORMULA Dalton Index
def dalton(array,eps):
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    #Media
    media=np.mean(array)
    # Dalton coefficient:
    return(1-((1/n)*((np.sum(((array)**(1-eps))-1))/((media**(1-eps))-1))))
  


#FORMULA Atkinson Index
def atkinson(array,eps):
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    #Media
    media=np.mean(array)


    # Atkinson coefficient:
    return(1-((1/n)*(np.sum((array/media)**(1-eps))))**(1/(1-eps)))


#FORMULA Shannon Index
def shannon(array):
    array = array.flatten()
    if np.amin(array) < 0:
        # Values cannot be negative:
        array -= np.amin(array)
    # Values cannot be 0:
    array += 0.0000001
    # Values must be sorted:
    array = np.sort(array)
    # Index per array element:
    index = np.arange(1,array.shape[0]+1)
    # Number of array elements:
    n = array.shape[0]
    # Shannon coefficient:
    return (np.sum((array/(np.sum(array)))*ln((np.sum(array))/array)*(1/(ln(n)))))