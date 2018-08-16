balance = 320000
annualInterestRate = 0.2

minimumMonthlyPayment = 10

monthlyInterestRate = annualInterestRate / 12

totalPaid = 0
startBalance = balance
itr = 0

MP_lowerBound = balance / 12
MP_upperBound = (balance*(1+monthlyInterestRate)**12) / 12
#minimumMonthlyPayment += (MP_lowerBound + MP_upperBound)/2

while True:
    minimumMonthlyPayment = (MP_lowerBound + MP_upperBound)/2
    #balance = startBalance
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
    #for
    
    if abs(balance) < 0.01:
        break
    elif balance < 0:
        MP_upperBound = minimumMonthlyPayment
        balance = startBalance
    elif balance > 0:
        MP_lowerBound = minimumMonthlyPayment
        balance = startBalance
#while    
#print '\nInitial loan: '  +  str(round(startBalance,2))
print('Lowest payment: '),
print(round(minimumMonthlyPayment,2))

#print '\nTotal paid: '  +  str(round(totalPaid,2))
#print 'Remaining balance: ' + str(round(balance,2))
#print 'Number of iterations: ' + str(itr)