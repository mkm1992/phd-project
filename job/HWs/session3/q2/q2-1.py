# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:57:36 2021

@author: 
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
from sklearn import svm  
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB
from scipy.stats.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve, auc, roc_curve
from sklearn.tree import DecisionTreeClassifier, export_graphviz


df = pd.read_csv (r'task.csv')

print(df.shape)
print(df.isnull().values.any())

def visuvalize_data(df):
	X = df['city'].values[:]  # we only take the first two features.
	y = df['view_count'].values[:]
	plt.scatter(X, y)
	plt.xlabel('city')
	plt.ylabel('view count')
	plt.title('city vs view')
	plt.show()
 
visuvalize_data(df)