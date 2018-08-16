count = 0
low = 0
high = 100
ans = (high + low) / 2
print ('Please think of a number between 0 and 100!')

while True:
    print 'Is your secret number ' + str(ans) + '?'
    print 'Enter "h" to indicate the guess is too high. ',
    print 'Enter "l" to indicate the guess is too low. ',
    print 'Enter "c" to indicate I guessed correctly. ',
    var = raw_input()
    
    if var == 'h':
        high = ans
    elif var == 'l':
        low = ans
    elif var == 'c':
        break
    else:
        print ('Sorry, I did not understand your input.')
    
    ans = (high + low) / 2
    count += 1

print 'Game over. Your secret number was: ' + str(ans)