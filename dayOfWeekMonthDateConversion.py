# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:34:26 2017

@author: chionic
"""
#code to get the day of the week and the month from a date string in format 'dd/mm/yyyy'
import time
import numpy as np

#importing the dates
dates = np.genfromtxt("D:\AIB dtatathon\DataHack 2017\DataHack 2017\DataHack 2017 Data\Bikes1.csv",delimiter=',', dtype=None)

day = list()
month = list()

#for each date in dates, find the day of the week and the month
for i in range(0,dates.size):
    x= time.strftime("%a", time.strptime(dates[i], "%d/%m/%Y"))
    z= time.strftime("%m", time.strptime(dates[i], "%d/%m/%Y"))
    
    if x == 'Mon':
        y = 0;    
    elif x == 'Tue':
        y = 1;                  
    elif x == 'Wed':
        y = 2;    
    elif x == 'Thu':
        y = 3;  
    elif x == 'Fri':
        y = 4;  
    elif x == 'Sat':
        y = 5;  
    elif x == 'Sun':
        y = 6;  
    #add it to the relevant list
    day.append(int(y))
    month.append(int(z))
    #print l, o
    
#output .csv files with the relevant data
np.savetxt("D:\AIB dtatathon\DataHack 2017\DataHack 2017\DataHack 2017 Data\month.csv", month, delimiter=",")
np.savetxt("D:\AIB dtatathon\DataHack 2017\DataHack 2017\DataHack 2017 Data\day_of_week.csv", day, delimiter=",")

