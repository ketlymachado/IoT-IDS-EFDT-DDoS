#########################################################################
#                                                                       #
# Project           : Network Intrusion Detection System for IoT        #
#                                                                       #
# Program name      : adasyn.py                                         #
#                                                                       #
# Authors           : Gustavo Vitral Arbex, Kétly Gonçalves Machado,    #
#                     Daniel Macêdo Batista, Roberto Hirata Junior      #
#                                                                       #
# Date created      : 20200617                                          #
#                                                                       #
# Purpose           : Uses the ADASYN sampling technique to equal the   #
#                     number of normal and attack instances.            #
#                                                                       #
#                     Some features were removed from the data in order #
#                     to perform the ADASYN method. This removal is     #
#                     explained in the paper.                           #
#                                                                       #
#########################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import ADASYN
from collections import Counter

data = pd.read_csv('bot-iot.csv')

cols = ['pkSeqID','stime','flgs','proto','saddr','sport','daddr','dport','pkts','bytes','state','ltime',
        'seq','dur','mean','stddev','smac','dmac','sum','min','max','soui','doui','sco','dco','spkts',
        'dpkts','sbytes','dbytes','rate','srate','drate','attack','category','subcategory']

data.columns = cols

# Checking data types

#data.info()

#print(data.head)

#print(data['attack'].value_counts())

# Checking NaN values in the data

#count_nan_in_df = data.isnull().sum()
#print (count_nan_in_df)

# Removing features from the data
botiot = data.drop(['pkSeqID','stime','flgs','proto','saddr','sport','daddr','dport','state','smac','dmac','soui','doui','sco','dco','category','subcategory'], axis=1)

# Dataframe to Numpy Arrays
X = botiot.iloc[:,:-1].values
y = botiot.iloc[:,-1].values

#print('Shape of Feature Matrix: ', X.shape)
#print('Shape of Target Vector: ', y.shape)

print('Original Target Variable Distribution: ', Counter(y))

ada = ADASYN(sampling_strategy = 'minority', n_neighbors = 5)

X_res, y_res = ada.fit_sample(X, y)

print('Oversampled Target Variable Distribution: ', Counter(y_res))