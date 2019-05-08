# -*- coding: utf-8 -*-
"""
Created on Sat May  4 10:18:06 2019

@author: Akash
"""
import pandas as pd
import pyowm
owm = pyowm.OWM('ee7951358c7149b30a9615cf1dbc9f4e')
nagpur,chennai , mumbai= owm.weather_at_place("nagpur,india"), owm.weather_at_place("chennai,india"),owm.weather_at_place("mumbai,india")
w,w1,w2 = nagpur.get_weather(),chennai.get_weather(), mumbai.get_weather()
temperature1,temperature2,temperature3 = w.get_temperature('celsius'),w1.get_temperature('celsius'),w2.get_temperature('celsius')
data = [['nagpur',temperature1 ], ['chennai', temperature2], ['Mumbai', temperature3]]
df = pd.DataFrame(data, columns = ['City', 'Temperature'])
