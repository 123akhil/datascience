s = 'pifpisdbobpoiuaspojdbobpoiasopibobobobpoasidbobpoaisbobobopoibob'
bob_count = 0
i = 0

while i <= len (s) -3 :
    x = s [i:i+3] 
    
    if x == 'bob':
        bob_count += 1

    i +=1

print 'Number of bobs: ' + str(bob_count)
