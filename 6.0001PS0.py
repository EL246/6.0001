#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:08:43 2017

@author: elana
"""
#asks user to enter number "x"
x = float(input("Enter number x:"))
print("x=", x)

#asks user to enter number "y"
y = float(input("Enter number y:"))


#prints x**y
print("x**y= ", x**y)

#prints logx
import numpy as np
logx= np.log2(x)
print("log(x) = ", logx)


