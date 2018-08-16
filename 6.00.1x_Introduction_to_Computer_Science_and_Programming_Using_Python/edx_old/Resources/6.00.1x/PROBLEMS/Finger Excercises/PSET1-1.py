s = 'aaaaaaaaaaaa'

vowel_count = 0

for x in s:
    
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        
        vowel_count += 1


print 'Number of vowels: ' + str(vowel_count)

