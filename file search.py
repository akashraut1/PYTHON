# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:51:08 2019

@author: Akash
"""

file = open("Akash.txt","r+") 
a=file.readlines()
#print(a)
for b in a :
    if b in "kartik\n":
        print("fsdfsd")

    else:
        l = "dfgd\n"
        file.write(l)
file.close()    
 