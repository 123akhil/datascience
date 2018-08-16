
balance = 4842.00
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

paid = 0.00

for month in range (1,13):
    
    print 'Month: ' + str(month)
    
    minimum_payment = round(balance*monthlyPaymentRate,2)

    print 'Minimum monthly payment: ' + str(minimum_payment)

    balance = (balance - minimum_payment) * (1+annualInterestRate/12)
    
    balance = round(balance,2)

    print 'Remaining balance: ' + str(balance)

    paid =  paid + minimum_payment   
    

print 'Total paid: ' + str(paid)

print 'Remaining balance: ' + str(balance)
            #Month: 1
	    # Minimum monthly payment: 168.52
	    # Remaining balance: 4111.89