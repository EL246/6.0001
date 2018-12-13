#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:35:19 2017

@author: elana
"""

#known variables
portion_down_payment = 0.25
r=0.04
annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
steps=0
savings=0


# total house downpayment = total_cost*portion_down_payment
# annual_salary*portion_saved*

reqd_cash = total_cost*portion_down_payment
high=10000
low=0
#print("abs saving-reqd cash = ", abs(savings-reqd_cash))
while abs(savings-reqd_cash) >= 100 and high>low:
    salary = annual_salary
    savings=0
    guess = (high+low)/2
    print("guess=", guess)
    steps += 1
    for i in range(36):
        savings += savings*r/12
        savings += salary*guess/(12*10000)
        if i%6 ==0:
            salary += salary*semi_annual_raise
        print("i= ",  i, "savings= ", savings)
    if savings < reqd_cash:
        low=guess
    else:
        high=guess
        
if abs(savings-reqd_cash) > 100:
    print("It is not possible to pay the down payment in 3 years")
else:
    print("Best savings rate: ", int(guess)/10000)
    print("Number of steps in bisectional search: ", steps)
    

