import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#########

df = pd.read_csv (r'StudentsPerformance.csv')
print(df.shape)
print(df.isnull().values.any())
#######

def visuvalize_data(df):
	X = df['gender'].values[:]  # we only take the first two features.
	y = df['math_score'].values[:]
	plt.scatter(X, y)
	plt.xlabel('gender')
	plt.ylabel('math_score')
	plt.title('gender vs math_score')
	plt.show()
 
visuvalize_data(df)

def visuvalize_data1(df):
	X = df['race'].values[:]  # we only take the first two features.
	y = df['math_score'].values[:]
	plt.scatter(X, y)
	plt.xlabel('race')
	plt.ylabel('math_score')
	plt.title('race vs math_score')
	plt.show()
 
visuvalize_data1(df)

###########

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





