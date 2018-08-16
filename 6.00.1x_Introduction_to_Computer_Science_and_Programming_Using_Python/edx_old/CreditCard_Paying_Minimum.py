# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 00:09:32 2016

@author: Camilo
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12
totalPaid = 0


for i in range(1,12+1):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    totalPaid = totalPaid + minimumMonthlyPayment
    #print 'Month: ' + str(i),
    #print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2))
    
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    #print ' Remaining balance: ' + str(round(balance,2))
    
#print '\nTotal paid: '  +  str(round(totalPaid,2))
print('Remaining balance: ') , 
print(round(balance,2))