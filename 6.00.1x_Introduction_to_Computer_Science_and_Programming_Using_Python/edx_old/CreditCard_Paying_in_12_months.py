# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 00:09:32 2016

@author: Camilo
"""

balance = 4773
annualInterestRate = 0.2

minimumMonthlyPayment = 10

monthlyInterestRate = annualInterestRate / 12
totalPaid = 0
startBalance = balance
itr = 0

while balance > 0:
    minimumMonthlyPayment += 10
    balance = startBalance
    totalPaid = 0
    for i in range(1,12+1):
        #minimumMonthlyPayment = monthlyPaymentRate * balance
        totalPaid = totalPaid + minimumMonthlyPayment
        #print 'Month: ' + str(i)
        #print 'Minimum monthly payment: ' + str(round(minimumMonthlyPayment,2))
        
        monthlyUnpaidBalance = balance - minimumMonthlyPayment
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        itr +=1
        
        #print 'Remaining balance: ' + str(round(balance,2))
        
#print '\nInitial loan: '  +  str(round(startBalance,2))
print('Lowest payment: '),
print(round(minimumMonthlyPayment,2))

#print '\nTotal paid: '  +  str(round(totalPaid,2))
#print 'Remaining balance: ' + str(round(balance,2))
#print 'Number of iterations: ' + str(itr)