
balance = 999999
annualInterestRate = 0.18

payment = 0.00

monthly_rate = (annualInterestRate)/12.0

upper_bound = (balance*(1+monthly_rate)**12)/12

lower_bound = balance / 12

unpaid_balance = balance

epsilon = 0.01

while    (upper_bound - lower_bound) > epsilon:
    
    payment = (lower_bound + upper_bound) / 2
   
    unpaid_balance = balance

    for month in range (1,13):
        
        unpaid_balance = unpaid_balance - payment
        
        unpaid_balance = unpaid_balance * (1+monthly_rate)
    
    if unpaid_balance > 0:
        lower_bound = payment
    elif unpaid_balance <= 0:
        upper_bound = payment
    
print 'Lowest payment: ' + str(round(payment,2))         
    