
balance = 999999
annualInterestRate = 0.18

payment = 0.00

monthly_rate = (annualInterestRate)/12.0


unpaid_balance = balance

while unpaid_balance > 0:
    
    payment = payment + 10.00
    
    unpaid_balance = balance

    for month in range (1,13):
      
        unpaid_balance = unpaid_balance - payment
        
        unpaid_balance = unpaid_balance * (1+monthly_rate)
    
    
    
print 'Lowest payment: ' + str(int(payment))

#Lowest Payment: 310