import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, binom, uniform, norm, poisson
from scipy.stats import norm, t, ttest_1samp, ttest_ind  

df=pd.read_csv('spam.csv',encoding='iso-8859-1')
#print(df.head())
df.drop('Unnamed: 2',axis=1,inplace=True)
df.drop('Unnamed: 3',axis=1,inplace=True)
df.drop('Unnamed: 4',axis=1,inplace=True)

for i in range (1,11):
   user_input=input("Enter q to quit ")
   print(df.v2.sample())
   if (user_input=='q'): 
    break
   
