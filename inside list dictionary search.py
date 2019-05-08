# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
Name=input("what is your name")
dicts = [{"name":"Akash","pass":"zzz"},{"name":"kartik","pass":"fcb"}]
def student(found):
    for found in dicts:
        if found["name"]  ==  Name:
            print(found)
        else :
            continue 
            
            
student('found')        
