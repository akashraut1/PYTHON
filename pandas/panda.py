# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:22:09 2019

@author: Akash
"""
import numpy as np
import pandas as pd
data =pd.read_csv(r'C:\Users\Akash\Desktop\abc.csv')
#b=data.loc[[9],['Value']]
#data = pd.read_excel(open('NSSC student Internship Details.xlsx', 'rb'))
#data=data.to_np()
#numpy_matrix = data.as_matrix()
#data=data.values
np_data = np.array(data.values)


#print(np_data[99,5])
b=data.loc[[99],['Value']]
print(b)