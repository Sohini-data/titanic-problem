# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:50:05 2019

@author: LENOVO
"""

#analytics tool
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


trainingdata = pd.read_csv('C:\\Users\\LENOVO\\Documents\\Projects\\titanic-problem\\data\\train.csv', sep=',')

print trainingdata.head(10)


#printing column names

print(trainingdata.columns.values)




