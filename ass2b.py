# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:21:07 2023

@author: USER
"""

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
