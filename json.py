# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:58:03 2019

@author: Akash
"""

#import numpy as np
import pandas as pd
data =pd.read_json(r'C:\Users\Akash\Desktop\ab.json')
#data = pd.read_excel(open('NSSC student Internship Details.xlsx', 'rb'))
a= data.loc[0]

print(data)