# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:47:29 2019

@author: Akash
"""

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
data =pd.read_csv(r'C:\Users\Akash\Desktop\abc.csv')
year=data["Year"]
cgpa=data["Value"]
plt.scatter(year, cgpa)
plt.xlabel('cgpa')
plt.ylabel('year')
plt.title('aise he')
plt.show()