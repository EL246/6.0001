#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 21:23:27 2017

@author: elana
"""
#variables
portion_down_payment = 0.25
current_savings=0
r=0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved= float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# total house downpayment = total_cost*portion_down_payment
# annual_salary*portion_saved*

reqd_cash = total_cost*portion_down_payment
i=0

while current_savings < reqd_cash:
    i += 1
    current_savings += current_savings*r/12
    current_savings += annual_salary*portion_saved/12
    
    

print("Number of months", i)
