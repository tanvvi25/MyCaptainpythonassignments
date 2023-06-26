# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 18:42:22 2023

@author: USER
"""

# print positive Numbers in a List
  
# input of list
li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)

print("Positive numbers in",li,"are: ")
  
#traversing
for i in li:   
    # checking condition
    if i >= 0:
       print(i, end = " ")


output
runfile('C:/Users/USER/untitled0.py', wdir='C:/Users/USER')
Enter size of list 5
Enter element of list 12 -7 5 64 -14
Traceback (most recent call last):

  File C:\Program Files\Spyder\pkgs\spyder_kernels\py3compat.py:356 in compat_exec
    exec(code, globals, locals)

  File c:\users\user\untitled0.py:14
    e=int(input("Enter element of list "))

ValueError: invalid literal for int() with base 10: '12 -7 5 64 -14'




runfile('C:/Users/USER/untitled0.py', wdir='C:/Users/USER')
Enter size of list 5
Enter element of list 12
Enter element of list -7
Enter element of list 5
Enter element of list 64
Enter element of list -14
Positive numbers in [12, -7, 5, 64, -14] are: 
12 5 64 

runfile('C:/Users/USER/untitled0.py', wdir='C:/Users/USER')
Enter size of list 4
Enter element of list 12
Enter element of list 14
Enter element of list -95
Enter element of list 3
Positive numbers in [12, 14, -95, 3] are: 
12 14 3 
