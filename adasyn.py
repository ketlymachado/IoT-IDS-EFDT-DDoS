#########################################################################
#                                                                       #
# Project           : Network Intrusion Detection System for IoT        #
#                                                                       #
# Program name      : adasyn.py                                         #
#                                                                       #
# Authors           : Gustavo Vitral Arbex, Kétly Gonçalves Machado,    #
#                     Daniel Macêdo Batista, Roberto Hirata Junior      #
#                                                                       #
# Purpose           : Uses the ADASYN sampling technique to balance the #
#                     number of normal and attack instances.            #
#                                                                       #
#                     Some features were removed from the data in order #
#                     to perform the ADASYN method.                     #
#                                                                       #
#                     After applying the ADASYN technique, it generates #
#                     a new .csv file with the resampled data.          #
#                                                                       #
#########################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from imblearn.over_sampling import ADASYN
from collections import Counter

data = pd.read_csv('botiot.csv')

cols = ['pkSeqID','stime','flgs','proto','saddr','sport','daddr','dport','pkts','bytes','state','ltime',
        'seq','dur','mean','stddev','smac','dmac','sum','min','max','soui','doui','sco','dco','spkts',
        'dpkts','sbytes','dbytes','rate','srate','drate','attack','category','subcategory']

data.columns = cols

print("\nChecking data types...\n")
data.info()

print("\nChecking for NaN values in the data...\n")
count_nan_in_df = data.isnull().sum()
print (count_nan_in_df)

print("\nRemoving categorical features and features with NaN values from the data...\n")
botiot = data.drop(['flgs','proto','saddr','sport','daddr','dport','state','smac','dmac',
                    'soui','doui','sco','dco','category','subcategory'], axis=1)

print("Turning Dataframe to Numpy Arrays...\n")
# All columns except the last
X = botiot.iloc[:,:-1].values
# Only the last column
y = botiot.iloc[:,-1].values

print(f"Shape of Feature Matrix: {X.shape}")
print(f"Shape of Target Vector: {y.shape}")

print()
print(f"Original Target Variable Distribution: {Counter(y)}")

adasyn = ADASYN(sampling_strategy = 'minority', n_neighbors = 5)

print("\nResampling the data...\n")
X_res, y_res = adasyn.fit_resample(X, y)

print(f"Resampled Target Variable Distribution: {Counter(y_res)}")

print("\nTurning Numpy Arrays to Dataframe...\n")

cols = ['pkSeqID','stime','pkts','bytes','ltime','seq','dur','mean','stddev','sum','min',
        'max','spkts','dpkts','sbytes','dbytes','rate','srate','drate']

botiot = pd.DataFrame(X_res, columns=cols)

botiot['attack'] = y_res

print("Shuffling the data rows...\n")
botiot = botiot.sample(frac=1)

botiot.to_csv('botiot-adasyn.csv', index = False)

print("Resampled dataset stored in botiot-adasyn.csv.")