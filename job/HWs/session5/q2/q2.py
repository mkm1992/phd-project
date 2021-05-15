import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#########

df = pd.read_csv (r'StudentsPerformance.csv')
print(df.shape)
print(df.isnull().values.any())
#######


df.hist()

####

size_pd = np.zeros(df.shape)
var1 = df.var()
mean1 = df.mean()
median1 = df.median()
print(df.head())

####

print(df.columns)

##########

df.describe()





