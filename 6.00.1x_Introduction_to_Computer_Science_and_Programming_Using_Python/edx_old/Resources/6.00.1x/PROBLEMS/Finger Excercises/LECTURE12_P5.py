def genPrimes():
    
    primeList = []
    
    number = 2
    
    while True:
        isPrime = True
        for prime in primeList:
            
            if number % prime == 0:
                isPrime = False
                
            
        if isPrime:
             primeList.append(number)
             yield number      
        
        number += 1