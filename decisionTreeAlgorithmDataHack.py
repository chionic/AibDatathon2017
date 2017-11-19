# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:11:06 2017

@author: chionic
"""

import pandas as pd
from sklearn.tree import DecisionTreeRegressor


#importing sample data
df = pd.read_csv('D:\AIB dtatathon\DataHack 2017\DataHack 2017\DataHack 2017 Data\main2.csv', header=None)

#solution data set up
solutionData = [None] * 727
solutionData = df[0]

#sample data set up - sample data is the combined data of main2, month and day_of_week
sampleData = pd.read_csv('D:\AIB dtatathon\DataHack 2017\DataHack 2017\DataHack 2017 Data\sampleData.csv', header=None)

#setting up machine learning algorithm, regr_1 is to help judge optimal tree depth
regr_1 = DecisionTreeRegressor(max_depth = 2)
regr_2 = DecisionTreeRegressor(max_depth = 10, min_samples_leaf=3)
regr_1.fit(sampleData, solutionData)
regr_2.fit(sampleData, solutionData)

#reading in the test cases data
test = pd.read_csv('D:\AIB dtatathon\DataHack 2017\DataHack 2017\DataHack 2017 Data\Final Test.csv')
#removing unwanted variables in our test set, such as snow_depth which we don't have sample data for
testFinal = test[['Weekday','Month','AWND','PRCP','SNOW','TAVG','TMAX','TMIN','Holiday']]

results1 = regr_1.predict(testFinal)
results2 = regr_2.predict(testFinal)
print(results1)
print(results2)

#creating and formatting our solution set to fit the format required for the datathon
d = {'col1': test['ID'], 'col2': results2}
number = pd.DataFrame(data = d )
print(number)
number.to_csv("D:\\AIB dtatathon\DataHack 2017\\DataHack 2017\DataHack 2017 Data\\resultAttempt.csv", sep=",",header=False,index=False)  

        
