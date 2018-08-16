
def countVow(string):
    count = 0
    for char in string:
        #print char, type(char)
        if char in 'aeiouAEIOU':
            count += 1
        #else:
            #continue
    return count

c = raw_input('Type a string: ')
print 'Number of vowels: ' + str(countVow(c))